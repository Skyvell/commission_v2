import pytest


@pytest.fixture
def expected_parsed_volume_targets_result():
    data = expected_values = [
        {'agent': 'MINI Agent 1', 'year_month': '2024-01', 'target': 1000000},
        {'agent': 'MINI Agent 1', 'year_month': '2024-02', 'target': 1100000},
        {'agent': 'MINI Agent 1', 'year_month': '2024-03', 'target': 1050000},
        {'agent': 'MINI Agent 1', 'year_month': '2024-04', 'target': 1000000},
        {'agent': 'MINI Agent 1', 'year_month': '2024-05', 'target': 1100000},
        {'agent': 'MINI Agent 1', 'year_month': '2024-06', 'target': 1050000},
        {'agent': 'MINI Agent 1', 'year_month': '2024-07', 'target': 1050000},
        {'agent': 'MINI Agent 1', 'year_month': '2024-08', 'target': 1050000},
        {'agent': 'MINI Agent 1', 'year_month': '2024-09', 'target': 1000000},
        {'agent': 'MINI Agent 1', 'year_month': '2024-10', 'target': 1000000},
        {'agent': 'MINI Agent 1', 'year_month': '2024-11', 'target': 1000000},
        {'agent': 'MINI Agent 1', 'year_month': '2024-12', 'target': 1000000},
        {'agent': 'MINI Agent 2', 'year_month': '2024-01', 'target': 950000},
        {'agent': 'MINI Agent 2', 'year_month': '2024-02', 'target': 950000},
        {'agent': 'MINI Agent 2', 'year_month': '2024-03', 'target': 950000},
        {'agent': 'MINI Agent 2', 'year_month': '2024-04', 'target': 750000},
        {'agent': 'MINI Agent 2', 'year_month': '2024-05', 'target': 850000},
        {'agent': 'MINI Agent 2', 'year_month': '2024-06', 'target': 1025000},
        {'agent': 'MINI Agent 2', 'year_month': '2024-07', 'target': 1025000},
        {'agent': 'MINI Agent 2', 'year_month': '2024-08', 'target': 1025000},
        {'agent': 'MINI Agent 2', 'year_month': '2024-09', 'target': 1000000},
        {'agent': 'MINI Agent 2', 'year_month': '2024-10', 'target': 1100000},
        {'agent': 'MINI Agent 2', 'year_month': '2024-11', 'target': 1025000},
        {'agent': 'MINI Agent 2', 'year_month': '2024-12', 'target': 1025000},
        {'agent': 'MINI Agent 3', 'year_month': '2024-01', 'target': 500000},
        {'agent': 'MINI Agent 3', 'year_month': '2024-02', 'target': 550000},
        {'agent': 'MINI Agent 3', 'year_month': '2024-03', 'target': 450000},
        {'agent': 'MINI Agent 3', 'year_month': '2024-04', 'target': 500000},
        {'agent': 'MINI Agent 3', 'year_month': '2024-05', 'target': 550000},
        {'agent': 'MINI Agent 3', 'year_month': '2024-06', 'target': 350000},
        {'agent': 'MINI Agent 3', 'year_month': '2024-07', 'target': 450000},
        {'agent': 'MINI Agent 3', 'year_month': '2024-08', 'target': 500000},
        {'agent': 'MINI Agent 3', 'year_month': '2024-09', 'target': 500000},
        {'agent': 'MINI Agent 3', 'year_month': '2024-10', 'target': 550000},
        {'agent': 'MINI Agent 3', 'year_month': '2024-11', 'target': 450000},
        {'agent': 'MINI Agent 3', 'year_month': '2024-12', 'target': 400000},
        {'agent': 'MINI Agent 4', 'year_month': '2024-01', 'target': 1050000},
        {'agent': 'MINI Agent 4', 'year_month': '2024-02', 'target': 1050000},
        {'agent': 'MINI Agent 4', 'year_month': '2024-03', 'target': 1050000},
        {'agent': 'MINI Agent 4', 'year_month': '2024-04', 'target': 1000000},
        {'agent': 'MINI Agent 4', 'year_month': '2024-05', 'target': 1100000},
        {'agent': 'MINI Agent 4', 'year_month': '2024-06', 'target': 1050000},
        {'agent': 'MINI Agent 4', 'year_month': '2024-07', 'target': 1100000},
        {'agent': 'MINI Agent 4', 'year_month': '2024-08', 'target': 1100000},
        {'agent': 'MINI Agent 4', 'year_month': '2024-09', 'target': 1025000},
        {'agent': 'MINI Agent 4', 'year_month': '2024-10', 'target': 950000},
        {'agent': 'MINI Agent 4', 'year_month': '2024-11', 'target': 1025000},
        {'agent': 'MINI Agent 4', 'year_month': '2024-12', 'target': 950000},
        {'agent': 'MINI Agent 5', 'year_month': '2024-01', 'target': 950000},
        {'agent': 'MINI Agent 5', 'year_month': '2024-02', 'target': 1025000},
        {'agent': 'MINI Agent 5', 'year_month': '2024-03', 'target': 950000},
        {'agent': 'MINI Agent 5', 'year_month': '2024-04', 'target': 950000},
        {'agent': 'MINI Agent 5', 'year_month': '2024-05', 'target': 1025000},
        {'agent': 'MINI Agent 5', 'year_month': '2024-06', 'target': 950000},
        {'agent': 'MINI Agent 5', 'year_month': '2024-07', 'target': 975000},
        {'agent': 'MINI Agent 5', 'year_month': '2024-08', 'target': 1000000},
        {'agent': 'MINI Agent 5', 'year_month': '2024-09', 'target': 1100000},
        {'agent': 'MINI Agent 5', 'year_month': '2024-10', 'target': 1050000},
        {'agent': 'MINI Agent 5', 'year_month': '2024-11', 'target': 1050000},
        {'agent': 'MINI Agent 5', 'year_month': '2024-12', 'target': 1050000},
        {'agent': 'MINI Agent 6', 'year_month': '2024-01', 'target': 1100000},
        {'agent': 'MINI Agent 6', 'year_month': '2024-02', 'target': 1050000},
        {'agent': 'MINI Agent 6', 'year_month': '2024-03', 'target': 1050000},
        {'agent': 'MINI Agent 6', 'year_month': '2024-04', 'target': 950000},
        {'agent': 'MINI Agent 6', 'year_month': '2024-05', 'target': 1000000},
        {'agent': 'MINI Agent 6', 'year_month': '2024-06', 'target': 1100000},
        {'agent': 'MINI Agent 6', 'year_month': '2024-07', 'target': 950000},
        {'agent': 'MINI Agent 6', 'year_month': '2024-08', 'target': 950000},
        {'agent': 'MINI Agent 6', 'year_month': '2024-09', 'target': 1050000},
        {'agent': 'MINI Agent 6', 'year_month': '2024-10', 'target': 1100000},
        {'agent': 'MINI Agent 6', 'year_month': '2024-11', 'target': 1100000},
        {'agent': 'MINI Agent 6', 'year_month': '2024-12', 'target': 1050000},
        {'agent': 'MINI Agent 7', 'year_month': '2024-01', 'target': 225000},
        {'agent': 'MINI Agent 7', 'year_month': '2024-02', 'target': 175000},
        {'agent': 'MINI Agent 7', 'year_month': '2024-03', 'target': 200000},
        {'agent': 'MINI Agent 7', 'year_month': '2024-04', 'target': 210000},
        {'agent': 'MINI Agent 7', 'year_month': '2024-05', 'target': 205000},
        {'agent': 'MINI Agent 7', 'year_month': '2024-06', 'target': 185000},
        {'agent': 'MINI Agent 7', 'year_month': '2024-07', 'target': 195000},
        {'agent': 'MINI Agent 7', 'year_month': '2024-08', 'target': 215000},
        {'agent': 'MINI Agent 7', 'year_month': '2024-09', 'target': 210000},
        {'agent': 'MINI Agent 7', 'year_month': '2024-10', 'target': 205000},
        {'agent': 'MINI Agent 7', 'year_month': '2024-11', 'target': 185000},
        {'agent': 'MINI Agent 7', 'year_month': '2024-12', 'target': 195000},
        {'agent': 'MINI Agent 8', 'year_month': '2024-01', 'target': 500000},
        {'agent': 'MINI Agent 8', 'year_month': '2024-02', 'target': 500000},
        {'agent': 'MINI Agent 8', 'year_month': '2024-03', 'target': 550000},
        {'agent': 'MINI Agent 8', 'year_month': '2024-04', 'target': 450000},
        {'agent': 'MINI Agent 8', 'year_month': '2024-05', 'target': 400000},
        {'agent': 'MINI Agent 8', 'year_month': '2024-06', 'target': 375000},
        {'agent': 'MINI Agent 8', 'year_month': '2024-07', 'target': 400000},
        {'agent': 'MINI Agent 8', 'year_month': '2024-08', 'target': 500000},
        {'agent': 'MINI Agent 8', 'year_month': '2024-09', 'target': 550000},
        {'agent': 'MINI Agent 8', 'year_month': '2024-10', 'target': 375000},
        {'agent': 'MINI Agent 8', 'year_month': '2024-11', 'target': 400000},
        {'agent': 'MINI Agent 8', 'year_month': '2024-12', 'target': 400000},
        {'agent': 'MINI Agent 9', 'year_month': '2024-01', 'target': 450000},
        {'agent': 'MINI Agent 9', 'year_month': '2024-02', 'target': 400000},
        {'agent': 'MINI Agent 9', 'year_month': '2024-03', 'target': 500000},
        {'agent': 'MINI Agent 9', 'year_month': '2024-04', 'target': 500000},
        {'agent': 'MINI Agent 9', 'year_month': '2024-05', 'target': 550000},
        {'agent': 'MINI Agent 9', 'year_month': '2024-06', 'target': 450000},
        {'agent': 'MINI Agent 9', 'year_month': '2024-07', 'target': 400000},
        {'agent': 'MINI Agent 9', 'year_month': '2024-08', 'target': 500000},
        {'agent': 'MINI Agent 9', 'year_month': '2024-09', 'target': 550000},
        {'agent': 'MINI Agent 9', 'year_month': '2024-10', 'target': 375000},
        {'agent': 'MINI Agent 9', 'year_month': '2024-11', 'target': 400000},
        {'agent': 'MINI Agent 9', 'year_month': '2024-12', 'target': 350000},
        {'agent': 'MINI Agent 10', 'year_month': '2024-01', 'target': 750000},
        {'agent': 'MINI Agent 10', 'year_month': '2024-02', 'target': 800000},
        {'agent': 'MINI Agent 10', 'year_month': '2024-03', 'target': 750000},
        {'agent': 'MINI Agent 10', 'year_month': '2024-04', 'target': 800000},
        {'agent': 'MINI Agent 10', 'year_month': '2024-05', 'target': 750000},
        {'agent': 'MINI Agent 10', 'year_month': '2024-06', 'target': 800000},
        {'agent': 'MINI Agent 10', 'year_month': '2024-07', 'target': 750000},
        {'agent': 'MINI Agent 10', 'year_month': '2024-08', 'target': 800000},
        {'agent': 'MINI Agent 10', 'year_month': '2024-09', 'target': 750000},
        {'agent': 'MINI Agent 10', 'year_month': '2024-10', 'target': 800000},
        {'agent': 'MINI Agent 10', 'year_month': '2024-11', 'target': 750000},
        {'agent': 'MINI Agent 10', 'year_month': '2024-12', 'target': 800000},
    ]
    return data