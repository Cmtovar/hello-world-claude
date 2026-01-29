/**
 * TestBuilder - Factory pattern for creating movement mechanic tests
 *
 * Usage:
 * const test = new TestBuilder('testMyMechanic')
 *   .setMechanic('basic_movement')
 *   .setPlayerStart(0, 1, 0)
 *   .setGoal(2, 1, 0)
 *   .addGroundTile(0, 0, 0)
 *   .addGroundTile(1, 0, 0)
 *   .addGroundTile(2, 0, 0)
 *   .setExpectedInputs(['w', 'w'])
 *   .setConstraints({ allowedInputs: ['w', 's', 'a', 'd'] })
 *   .build();
 */

class TestBuilder {
    constructor(testName) {
        this.testData = {
            name: testName || 'Unnamed Test',
            description: '',
            mechanic: '',
            playerStart: { x: 0, y: 1, z: 0 },
            goal: null,
            voxels: [],
            expectedInputs: [],
            constraints: {},
            notes: ''
        };

        // Flyweight pools for reusable geometry
        this.colorPalette = {
            green: 65280,       // 0x00FF00
            orange: 16753920,   // 0xFFA500
            gray: 11184810,     // 0xAABBAA
            darkGray: 4210752,  // 0x404040
            red: 16711680,      // 0xFF0000
            blue: 255,          // 0x0000FF
            yellow: 16776960    // 0xFFFF00
        };
    }

    /**
     * Set the mechanic being tested
     */
    setMechanic(mechanicId) {
        this.testData.mechanic = mechanicId;
        return this;
    }

    /**
     * Set test description
     */
    setDescription(desc) {
        this.testData.description = desc;
        return this;
    }

    /**
     * Set player starting position
     */
    setPlayerStart(x, y, z) {
        this.testData.playerStart = { x, y, z };
        return this;
    }

    /**
     * Set goal position (optional)
     */
    setGoal(x, y, z) {
        this.testData.goal = { x, y, z };
        return this;
    }

    /**
     * Add a single voxel
     */
    addVoxel(x, y, z, color) {
        this.testData.voxels.push({
            x, y, z,
            color: typeof color === 'string' ? this.colorPalette[color] : color
        });
        return this;
    }

    /**
     * Add a ground tile (common pattern)
     */
    addGroundTile(x, z, color = 'green') {
        return this.addVoxel(x, 0, z, color);
    }

    /**
     * Add a platform at specific height
     */
    addPlatformTile(x, y, z, color = 'orange') {
        return this.addVoxel(x, y, z, color);
    }

    /**
     * Add a vertical column (pillar)
     */
    addColumn(x, z, startY, endY, color = 'gray') {
        for (let y = startY; y <= endY; y++) {
            this.addVoxel(x, y, z, color);
        }
        return this;
    }

    /**
     * Add a flat platform (rectangle)
     */
    addFlatPlatform(startX, endX, startZ, endZ, y, color = 'green') {
        for (let x = startX; x <= endX; x++) {
            for (let z = startZ; z <= endZ; z++) {
                this.addVoxel(x, y, z, color);
            }
        }
        return this;
    }

    /**
     * Add stairs (ascending in X direction)
     */
    addStairs(startX, endX, startY, z, color = 'orange') {
        let currentY = startY;
        for (let x = startX; x <= endX; x++) {
            for (let y = 0; y <= currentY; y++) {
                this.addVoxel(x, y, z, color);
            }
            currentY++;
        }
        return this;
    }

    /**
     * Add expected inputs (what keys should be pressed)
     */
    setExpectedInputs(inputs) {
        this.testData.expectedInputs = inputs;
        return this;
    }

    /**
     * Add constraints (declarative test rules)
     */
    setConstraints(constraints) {
        this.testData.constraints = {
            ...this.testData.constraints,
            ...constraints
        };
        return this;
    }

    /**
     * Add notes
     */
    addNotes(notes) {
        this.testData.notes = notes;
        return this;
    }

    /**
     * Validate test quality
     */
    validate() {
        const errors = [];

        if (!this.testData.mechanic) {
            errors.push('Mechanic ID is required');
        }

        if (this.testData.voxels.length === 0) {
            errors.push('At least one voxel is required');
        }

        // Check player start is valid
        const playerY = this.testData.playerStart.y;
        const playerX = this.testData.playerStart.x;
        const playerZ = this.testData.playerStart.z;

        const hasGroundBelowPlayer = this.testData.voxels.some(v =>
            v.x === playerX && v.z === playerZ && v.y === playerY - 1
        );

        if (!hasGroundBelowPlayer && playerY > 0) {
            errors.push(`Player start (${playerX}, ${playerY}, ${playerZ}) has no ground below`);
        }

        // Check goal is valid if present
        if (this.testData.goal) {
            const goalY = this.testData.goal.y;
            const goalX = this.testData.goal.x;
            const goalZ = this.testData.goal.z;

            const hasGroundBelowGoal = this.testData.voxels.some(v =>
                v.x === goalX && v.z === goalZ && v.y === goalY - 1
            );

            if (!hasGroundBelowGoal && goalY > 0) {
                errors.push(`Goal (${goalX}, ${goalY}, ${goalZ}) has no ground below`);
            }
        }

        // Check expected inputs are valid
        const validKeys = ['w', 's', 'a', 'd', 'Space', 'Shift', ' '];
        const validCombos = /^[wsad]\+[wsad]$/; // e.g., "w+d"

        this.testData.expectedInputs.forEach((input, i) => {
            if (!validKeys.includes(input) && !validCombos.test(input)) {
                errors.push(`Invalid input at index ${i}: "${input}"`);
            }
        });

        return {
            valid: errors.length === 0,
            errors
        };
    }

    /**
     * Build and return the test JSON
     */
    build() {
        const validation = this.validate();

        if (!validation.valid) {
            console.error('Test validation failed:');
            validation.errors.forEach(err => console.error('  -', err));
            throw new Error('Test validation failed. See console for details.');
        }

        return JSON.stringify(this.testData, null, 2);
    }

    /**
     * Build and save to file (Node.js only)
     */
    async saveToFile(filename) {
        const json = this.build();
        // This would use fs.writeFile in Node.js
        console.log('Generated test:', filename);
        console.log(json);
        return json;
    }
}

// Export for use in Node.js or browser
if (typeof module !== 'undefined' && module.exports) {
    module.exports = TestBuilder;
}

/**
 * Example Usage:
 *
 * // Simple flat movement test
 * const basicTest = new TestBuilder('testBasicMovement')
 *   .setMechanic('basic_movement')
 *   .setDescription('Walk forward on flat terrain')
 *   .setPlayerStart(0, 1, 0)
 *   .setGoal(2, 1, 0)
 *   .addFlatPlatform(-2, 2, -2, 2, 0, 'green')
 *   .setExpectedInputs(['w', 'w'])
 *   .build();
 *
 * // Staircase test
 * const stairTest = new TestBuilder('testAutoClimbStairs')
 *   .setMechanic('auto_climb')
 *   .setDescription('Auto-climb up stairs')
 *   .setPlayerStart(-2, 1, 0)
 *   .setGoal(2, 5, 0)
 *   .addStairs(-2, 2, 0, 0, 'orange')
 *   .setExpectedInputs(['w', 'w', 'w', 'w'])
 *   .setConstraints({
 *     autoClimbRequired: true
 *   })
 *   .build();
 *
 * // Diagonal movement test with constraints
 * const diagTest = new TestBuilder('testDiagonalOnly')
 *   .setMechanic('diagonal_movement')
 *   .setDescription('Only allow diagonal movement')
 *   .setPlayerStart(0, 1, 0)
 *   .setGoal(2, 1, 2)
 *   .addFlatPlatform(0, 2, 0, 2, 0, 'green')
 *   .setExpectedInputs(['w+d', 'w+d'])
 *   .setConstraints({
 *     allowedInputs: ['w+d', 'w+a', 's+d', 's+a'],
 *     blockCardinal: true
 *   })
 *   .build();
 */
