select person_name
from (
    select
        person_name,
        sum(weight) over (order by turn) as total_weight
    from queue
)As q
where total_weight <= 1000
order by total_weight DESC
limit 1;