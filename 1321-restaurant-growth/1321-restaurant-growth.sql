WITH daily AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),
running AS (
    SELECT
        visited_on,
        amount,
        SUM(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS total_amount,
        COUNT(*) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS days_count
    FROM daily
)
SELECT
    visited_on,
    total_amount AS amount,
    ROUND(total_amount / 7.0, 2) AS average_amount
FROM running
WHERE days_count = 7
ORDER BY visited_on;