import { test, expect } from '@playwright/test';
import {
  waitForGameReady,
  getPlayerPosition,
  isPlayerAtGoal,
  pressKeyForDuration,
  waitForPositionChange
} from '../helpers/test-utils.js';

test.describe('Descend Mechanic', () => {
  test('testDescendOneBlock - Player can descend 1 block', async ({ page }) => {
    // Load test map
    await page.goto('/?test=testDescendOneBlock');

    // Wait for game to be ready
    await waitForGameReady(page);

    // Get starting position
    const startPos = await getPlayerPosition(page);
    console.log('Starting position:', startPos);

    // Expected starting position
    expect(startPos.x).toBeCloseTo(0, 0);
    expect(startPos.y).toBeCloseTo(2, 0);
    expect(startPos.z).toBeCloseTo(0, 0);

    // Press Shift key to descend
    await pressKeyForDuration(page, 'Shift', 500);

    // Wait for position change
    const positionChanged = await waitForPositionChange(page, 2000);
    expect(positionChanged).toBe(true);

    // Give time for descent animation
    await page.waitForTimeout(500);

    // Get final position
    const finalPos = await getPlayerPosition(page);
    console.log('Final position:', finalPos);

    // Expected final position (y should be 1)
    expect(finalPos.x).toBeCloseTo(0, 0);
    expect(finalPos.y).toBeCloseTo(1, 1); // 5% tolerance
    expect(finalPos.z).toBeCloseTo(0, 0);

    // Check if player reached goal
    const reachedGoal = await isPlayerAtGoal(page);
    expect(reachedGoal).toBe(true);
  });

  test('testDescendOneBlock - Player cannot descend into solid voxel', async ({ page }) => {
    // This test ensures player doesn't phase through solid terrain
    await page.goto('/?test=testDescendOneBlock');
    await waitForGameReady(page);

    // First descend to y=1
    await pressKeyForDuration(page, 'Shift', 500);
    await page.waitForTimeout(500);

    const posAfterFirstDescend = await getPlayerPosition(page);
    expect(posAfterFirstDescend.y).toBeCloseTo(1, 1);

    // Try to descend again (should fail - there's a voxel at y=0)
    await pressKeyForDuration(page, 'Shift', 500);
    await page.waitForTimeout(500);

    const finalPos = await getPlayerPosition(page);

    // Player should still be at y=1 (can't descend into the voxel)
    expect(finalPos.y).toBeCloseTo(1, 1);
  });
});
