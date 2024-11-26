-- Create target schema in synapse db if it does not
  IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'dbo')
  BEGIN
    EXEC('CREATE SCHEMA [dbo]')
  END

  
    

    
    EXEC('create view 
      dbo.testview_12700
     as 
    
    

with all_values as (

    select
        status as value_field,
        count(*) as n_records

    from "dbo"."stg_orders"
    group by status

)

select *
from all_values
where value_field not in (
    ''placed'',''shipped'',''completed'',''return_pending'',''returned''
)


;')
    select
      
      count(*) as failures,
      case when count(*) != 0
        then 'true' else 'false' end as should_warn,
      case when count(*) != 0
        then 'true' else 'false' end as should_error
    from (
      select * from 
      dbo.testview_12700
    
    ) dbt_internal_test;

    EXEC('drop view 
      dbo.testview_12700
    ;')

  