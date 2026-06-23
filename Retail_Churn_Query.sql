WITH PremiumCustomers AS (
    SELECT customer_id, city
    FROM customers
    WHERE tier = 'Premium'
),
TicketStats AS (
    SELECT 
        customer_id,
        COUNT(ticket_id) AS total_tickets,
        AVG(days_to_resolve) AS avg_resolution_time
    FROM support_logs
    WHERE issue_type = 'Shipping Delay'
    GROUP BY customer_id
)
SELECT 
    CASE 
        WHEN t.avg_resolution_time > 3 THEN 'Over 3 Days'
        ELSE '3 Days or Under' 
    END AS delay_severity,
    COUNT(s.customer_id) AS total_premium_customers,
    SUM(CASE WHEN s.status = 'Churned' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN s.status = 'Churned' THEN 1.0 ELSE 0.0 END) / COUNT(s.customer_id) * 100, 2) AS churn_rate_percentage
FROM subscriptions s
JOIN PremiumCustomers p ON s.customer_id = p.customer_id
LEFT JOIN TicketStats t ON s.customer_id = t.customer_id
GROUP BY 1
ORDER BY churn_rate_percentage DESC; 