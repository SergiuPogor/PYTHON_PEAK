# Code Example: Testing Asynchronous Functions with Pytest

import pytest
import asyncio
import aiohttp

# Install `pytest-asyncio` to enable async support in pytest
@pytest.mark.asyncio
async def test_fetch_data():
    # Simulate an async HTTP request
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/todos/1') as response:
            data = await response.json()
            assert data['id'] == 1
            assert 'title' in data

# Mocking an async function to test data handling
async def fetch_data(item_id):
    # Simulates fetching item data asynchronously
    await asyncio.sleep(0.1)  # Simulate async delay
    return {"id": item_id, "name": f"Item-{item_id}", "status": "active"}

@pytest.mark.asyncio
async def test_process_data():
    data = await fetch_data(5)
    assert data['id'] == 5
    assert data['status'] == 'active'
    assert "name" in data

# Async testing of a function with multiple await calls
async def process_items(items):
    results = []
    for item in items:
        data = await fetch_data(item)
        results.append(data)
    return results

@pytest.mark.asyncio
async def test_batch_processing():
    items = [1, 2, 3]
    result = await process_items(items)
    assert len(result) == 3
    assert all(isinstance(item, dict) for item in result)
    assert result[0]["id"] == 1