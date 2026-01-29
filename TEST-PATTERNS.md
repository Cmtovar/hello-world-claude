# Test Design Patterns

**Purpose:** Standardized templates and patterns for creating high-quality mechanic tests.

## TestBuilder Factory Pattern

### Overview

The `TestBuilder` class provides a code-level template for programmatically generating test maps with built-in quality control.

**Benefits:**
- ✅ Consistent test structure
- ✅ Validation catches common errors
- ✅ Reusable components (flyweight pattern for colors)
- ✅ Fluent API for readability
- ✅ Helper methods for common patterns

### Basic Usage

```javascript
const test = new TestBuilder('testMyMechanic')
    .setMechanic('basic_movement')
    .setDescription('Walk forward on flat terrain')
    .setPlayerStart(0, 1, 0)
    .setGoal(2, 1, 0)
    .addGroundTile(0, 0, 'green')
    .addGroundTile(1, 0, 'green')
    .addGroundTile(2, 0, 'green')
    .setExpectedInputs(['w', 'w'])
    .build();

// Save to file
fs.writeFileSync('test-maps/testMyMechanic.json', test);
```

### Available Methods

#### Setup
- `setMechanic(id)` - Link to mechanic in mechanics-graph.json
- `setDescription(text)` - Explain what this tests
- `addNotes(text)` - Implementation details

#### Positioning
- `setPlayerStart(x, y, z)` - Where player spawns
- `setGoal(x, y, z)` - Target position (optional)

#### Voxel Building
- `addVoxel(x, y, z, color)` - Single voxel
- `addGroundTile(x, z, color)` - Voxel at y=0
- `addPlatformTile(x, y, z, color)` - Elevated voxel
- `addColumn(x, z, startY, endY, color)` - Vertical pillar
- `addFlatPlatform(x1, x2, z1, z2, y, color)` - Rectangle
- `addStairs(startX, endX, startY, z, color)` - Ascending steps

#### Test Configuration
- `setExpectedInputs([keys])` - What to press in animation
- `setConstraints({...})` - Declarative rules

### Color Palette (Flyweight)

Predefined colors avoid magic numbers:

```javascript
.addVoxel(0, 0, 0, 'green')      // 65280
.addVoxel(0, 1, 0, 'orange')     // 16753920
.addVoxel(0, 0, 1, 'gray')       // 11184810
.addVoxel(0, 0, 2, 'darkGray')   // 4210752
.addVoxel(0, 0, 3, 'red')        // 16711680
.addVoxel(0, 0, 4, 'blue')       // 255
.addVoxel(0, 0, 5, 'yellow')     // 16776960
```

## Constraint System

Constraints are declared in JSON and enforced programmatically.

### Constraint Format

```json
{
  "constraints": {
    "allowedInputs": ["w+d", "w+a", "s+d", "s+a"],
    "blockCardinal": true,
    "maxMovements": 10,
    "timeLimit": null
  }
}
```

### Constraint Types

**Movement Restrictions:**
```javascript
.setConstraints({
    allowedInputs: ['w', 's'],        // Only forward/back
    blockCardinal: true,               // Block N/S/E/W
    blockDiagonal: true                // Block NE/NW/SE/SW
})
```

**Limits:**
```javascript
.setConstraints({
    maxMovements: 5,         // Only 5 moves allowed
    timeLimit: 30000,        // 30 seconds max (ms)
    requireGoalReach: true   // Must reach goal to pass
})
```

**Mechanic Requirements:**
```javascript
.setConstraints({
    autoClimbRequired: true,     // Must use auto-climb
    manualDescentOnly: true,     // Can't use auto-descent
    noGravity: true              // Disable gravity for this test
})
```

## Common Test Patterns

### Pattern 1: Flat Movement

```javascript
const flatTest = new TestBuilder('testFlatMovement')
    .setMechanic('basic_movement')
    .setPlayerStart(0, 1, 0)
    .setGoal(3, 1, 0)
    .addFlatPlatform(-1, 4, -1, 1, 0, 'green')
    .setExpectedInputs(['w', 'w', 'w'])
    .build();
```

**Use case:** Test basic WASD on level ground.

### Pattern 2: Elevation Change

```javascript
const elevTest = new TestBuilder('testElevationChange')
    .setMechanic('auto_descent')
    .setPlayerStart(-2, 2, 0)
    .setGoal(2, 1, 0)
    .addFlatPlatform(-2, -1, 0, 0, 1, 'orange')  // High platform
    .addFlatPlatform(0, 2, 0, 0, 0, 'green')     // Low platform
    .setExpectedInputs(['w', 'w', 'w', 'w'])
    .build();
```

**Use case:** Test auto-descent when terrain drops.

### Pattern 3: Obstacle Course

```javascript
const obstacleTest = new TestBuilder('testObstacleCourse')
    .setMechanic('auto_climb')
    .setPlayerStart(-3, 1, 0)
    .setGoal(3, 1, 0)
    .addFlatPlatform(-3, -2, 0, 0, 0, 'green')   // Start
    .addColumn(-1, 0, 0, 1, 'orange')             // Obstacle
    .addFlatPlatform(0, 3, 0, 0, 0, 'green')     // End
    .setExpectedInputs(['w', 'w', 'w', 'w', 'w', 'w'])
    .build();
```

**Use case:** Test auto-climb over single-block obstacles.

### Pattern 4: Diagonal Path

```javascript
const diagTest = new TestBuilder('testDiagonalPath')
    .setMechanic('diagonal_movement')
    .setPlayerStart(0, 1, 0)
    .setGoal(3, 1, 3)
    .addFlatPlatform(0, 3, 0, 3, 0, 'green')     // Square platform
    .setExpectedInputs(['w+d', 'w+d', 'w+d'])
    .setConstraints({
        allowedInputs: ['w+d', 'w+a', 's+d', 's+a'],
        blockCardinal: true
    })
    .build();
```

**Use case:** Test diagonal movement only (no cardinal).

### Pattern 5: Vertical Challenge

```javascript
const vertTest = new TestBuilder('testVerticalChallenge')
    .setMechanic('climb_up_one')
    .setPlayerStart(0, 1, 0)
    .setGoal(0, 4, 0)
    .addColumn(0, 0, 0, 3, 'orange')              // Tall pillar
    .addGroundTile(-1, 0, 'gray')                 // Surrounding
    .addGroundTile(1, 0, 'gray')
    .setExpectedInputs(['Space', 'Space', 'Space'])
    .build();
```

**Use case:** Test manual climb up multiple levels.

## Quality Control Checklist

The TestBuilder validates:

### Structural Checks
- ✅ Mechanic ID is set
- ✅ At least one voxel exists
- ✅ Player start has ground below (unless y=0)
- ✅ Goal has ground below (if present)
- ✅ All inputs are valid keys

### Logic Checks (Future)
- Path exists from start to goal
- Goal is reachable with given constraints
- No impossible jumps required
- Voxels don't overlap in invalid ways

### Style Checks (Future)
- Test name follows convention (`test[MechanicName]`)
- Description is clear and concise
- Colors are used consistently
- Map is minimal (no unnecessary voxels)

## Flyweight Pattern for Voxels

When creating many identical tiles, use flyweight to reduce memory:

### Current (No Flyweight)
```javascript
// Each voxel creates new geometry + material
for (let i = 0; i < 100; i++) {
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshLambertMaterial({ color: 0x00FF00 });
    const mesh = new THREE.Mesh(geometry, material);
}
// Memory: 100 geometries + 100 materials
```

### With Flyweight (Future)
```javascript
// Share geometry and materials
const cubeGeometry = new THREE.BoxGeometry(1, 1, 1);
const greenMaterial = new THREE.MeshLambertMaterial({ color: 0x00FF00 });

for (let i = 0; i < 100; i++) {
    const mesh = new THREE.Mesh(cubeGeometry, greenMaterial);
}
// Memory: 1 geometry + 1 material (99% reduction)
```

**When to implement:** After 20+ test maps with 500+ voxels total.

## Fuzzing (Future)

Generate random tests to find edge cases:

```javascript
class TestFuzzer {
    static generateRandomTest(mechanic, constraints) {
        const builder = new TestBuilder('testFuzzed_' + Date.now());

        // Random starting position
        const startX = Math.floor(Math.random() * 10) - 5;
        const startZ = Math.floor(Math.random() * 10) - 5;

        builder
            .setMechanic(mechanic)
            .setPlayerStart(startX, 1, startZ)
            .addGroundTile(startX, startZ, 'green');

        // Generate random platform
        for (let i = 0; i < 20; i++) {
            const x = Math.floor(Math.random() * 10) - 5;
            const z = Math.floor(Math.random() * 10) - 5;
            const y = Math.floor(Math.random() * 3);

            builder.addVoxel(x, y, z, 'green');
        }

        // Random goal
        const goalX = Math.floor(Math.random() * 10) - 5;
        const goalZ = Math.floor(Math.random() * 10) - 5;
        builder.setGoal(goalX, 1, goalZ);
        builder.addGroundTile(goalX, goalZ, 'orange');

        return builder.build();
    }
}

// Generate 100 random tests
for (let i = 0; i < 100; i++) {
    const test = TestFuzzer.generateRandomTest('basic_movement', {});
    // Run test, collect results
}
```

**Use case:** Discover unexpected bugs that hand-crafted tests miss.

## Example: Complete Test Creation

```javascript
// 1. Define what we're testing
const mechanic = 'walk_down_terrain';

// 2. Use builder to create test
const test = new TestBuilder('testWalkDownSlope')
    .setMechanic(mechanic)
    .setDescription('Player walks down a gentle slope')
    .setPlayerStart(-3, 3, 0)
    .setGoal(3, 1, 0)
    // Build descending terrain
    .addFlatPlatform(-3, -3, 0, 0, 2, 'orange')  // y=2
    .addFlatPlatform(-2, -2, 0, 0, 2, 'orange')
    .addFlatPlatform(-1, -1, 0, 0, 1, 'orange')  // y=1
    .addFlatPlatform(0, 0, 0, 0, 1, 'orange')
    .addFlatPlatform(1, 3, 0, 0, 0, 'green')     // y=0
    .setExpectedInputs(['w', 'w', 'w', 'w', 'w', 'w'])
    .setConstraints({
        requireGoalReach: true,
        autoDescentRequired: true
    })
    .addNotes('Tests smooth auto-descent over gradual slope')
    .build();

// 3. Save to file
fs.writeFileSync('test-maps/testWalkDownSlope.json', test);

// 4. Update mechanics graph
// (Manually add test to mechanics-graph.json)

// 5. Test it!
// Open http://localhost:8080/ and select "Walk Down Slope" test
```

## Best Practices

### DO:
- ✅ Use TestBuilder for all new tests
- ✅ Validate tests before committing
- ✅ Use color names, not numbers
- ✅ Add constraints for focused testing
- ✅ Keep maps minimal (only necessary voxels)
- ✅ Test one mechanic per map

### DON'T:
- ❌ Create tests manually (error-prone)
- ❌ Skip validation
- ❌ Use magic numbers for colors
- ❌ Create giant maps for simple tests
- ❌ Test multiple mechanics in one map

## Next Steps

1. **Implement constraint enforcement** - Make constraints actually restrict movement
2. **Add path validation** - Check if goal is reachable
3. **Create fuzzer** - Generate random tests automatically
4. **Implement flyweight** - Share geometry/materials
5. **Add test templates** - Pre-built patterns for common scenarios

---

**See Also:**
- `test-builder.js` - Factory implementation
- `METHODOLOGY.md` - Overall testing philosophy
- `mechanics-graph.json` - Mechanic dependencies
