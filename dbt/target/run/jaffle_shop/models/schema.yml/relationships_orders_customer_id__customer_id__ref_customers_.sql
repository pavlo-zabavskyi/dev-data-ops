-- Create target schema in synapse db if it does not
  IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'dbo')
  BEGIN
    EXEC('CREATE SCHEMA [dbo]')
  END

  
    

    
    EXEC('create view 
      dbo.testview_17347
     as 
    
    

with child as (
    select customer_id as from_field
    from "dbo"."orders"
    where customer_id is not null
),

parent as (
    select customer_id as to_field
    from "dbo"."customers"
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


;')
    select
      
      count(*) as failures,
      case when count(*) != 0
        then 'true' else 'false' end as should_warn,
      case when count(*) != 0
        then 'true' else 'false' end as should_error
    from (
      select * from 
      dbo.testview_17347
    
    ) dbt_internal_test;

    EXEC('drop view 
      dbo.testview_17347
    ;')

  