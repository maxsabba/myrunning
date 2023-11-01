SELECT da.created_at , da.start_time , da.duration, di.distance 
FROM data_activity da 
inner join data_initialvalues di on da.id =di.activity_id 

WHERE da.id = '313a6dc2d3684c6799a2324c35a5edcd'




SELECT *
FROM data_initialvalues di 

