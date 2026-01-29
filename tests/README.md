# Game Mechanics Tests

Automated Playwright tests for validating 3D movement mechanics.

## Setup

```bash
cd tests
npm install
```

## Running Tests

```bash
# Run all tests
npm test

# Run with UI mode (visual debugging)
npm run test:ui

# Debug mode (step through)
npm run test:debug

# Run specific test file
npx playwright test specs/descend.spec.js
```

## Test Structure

- `specs/` - Test files organized by mechanic
- `helpers/` - Shared test utilities
- `../test-maps/` - JSON map configurations for isolated mechanic testing

## Writing New Tests

1. Create test map JSON in `test-maps/`
2. Create spec file in `specs/`
3. Use helpers from `test-utils.js`
4. Follow naming: `test{MechanicName}.json` and `{mechanic}.spec.js`

## Test Map Format

```json
{
  "name": "Test Name",
  "description": "What this tests",
  "mechanic": "mechanic_id",
  "playerStart": {"x": 0, "y": 1, "z": 0},
  "goal": {"x": 0, "y": 2, "z": 0},
  "voxels": [
    {"x": 0, "y": 0, "z": 0, "color": 0x808080}
  ]
}
```

## Position Validation

Tests use 5% total distance tolerance. Helper function `isPositionClose()` handles this calculation.

## Current Test Status

See `../mechanics-graph.json` for mechanic dependencies and test coverage.
