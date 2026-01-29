/**
 * Test utility functions for game mechanics validation
 */

/**
 * Wait for game to fully load and be ready
 * @param {import('@playwright/test').Page} page
 */
export async function waitForGameReady(page) {
  await page.waitForFunction(() => {
    return window.game &&
           window.game.scene &&
           window.game.player &&
           window.game.playerPos;
  }, { timeout: 10000 });

  // Give extra time for rendering
  await page.waitForTimeout(500);
}

/**
 * Get current player position
 * @param {import('@playwright/test').Page} page
 * @returns {Promise<{x: number, y: number, z: number}>}
 */
export async function getPlayerPosition(page) {
  return await page.evaluate(() => {
    return {
      x: window.game.playerPos.x,
      y: window.game.playerPos.y,
      z: window.game.playerPos.z
    };
  });
}

/**
 * Check if player is at goal position (5% tolerance)
 * @param {import('@playwright/test').Page} page
 * @returns {Promise<boolean>}
 */
export async function isPlayerAtGoal(page) {
  return await page.evaluate(() => {
    return window.isPlayerAtGoal();
  });
}

/**
 * Calculate 3D distance between two points
 * @param {{x: number, y: number, z: number}} pos1
 * @param {{x: number, y: number, z: number}} pos2
 * @returns {number}
 */
export function calculateDistance(pos1, pos2) {
  const dx = pos1.x - pos2.x;
  const dy = pos1.y - pos2.y;
  const dz = pos1.z - pos2.z;
  return Math.sqrt(dx * dx + dy * dy + dz * dz);
}

/**
 * Check if two positions are within 5% tolerance
 * @param {{x: number, y: number, z: number}} pos1
 * @param {{x: number, y: number, z: number}} pos2
 * @param {number} baseTolerance - Base tolerance value (default 1.0)
 * @returns {boolean}
 */
export function isPositionClose(pos1, pos2, baseTolerance = 1.0) {
  const distance = calculateDistance(pos1, pos2);
  const tolerance = Math.max(baseTolerance, distance * 0.05);
  return distance <= tolerance;
}

/**
 * Simulate key press for a duration
 * @param {import('@playwright/test').Page} page
 * @param {string} key - Key to press (e.g., 'w', 'Shift', ' ')
 * @param {number} duration - Duration in milliseconds
 */
export async function pressKeyForDuration(page, key, duration) {
  await page.keyboard.down(key);
  await page.waitForTimeout(duration);
  await page.keyboard.up(key);
}

/**
 * Wait for player position to change
 * @param {import('@playwright/test').Page} page
 * @param {number} timeout - Timeout in milliseconds
 * @returns {Promise<boolean>} - True if position changed
 */
export async function waitForPositionChange(page, timeout = 3000) {
  const startPos = await getPlayerPosition(page);

  const changed = await page.waitForFunction(
    (startPos) => {
      const current = window.game.playerPos;
      return current.x !== startPos.x ||
             current.y !== startPos.y ||
             current.z !== startPos.z;
    },
    startPos,
    { timeout }
  ).then(() => true).catch(() => false);

  return changed;
}
