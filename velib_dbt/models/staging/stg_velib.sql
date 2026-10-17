select
    stationcode::varchar as station_id,
    name::varchar as station_name,
    nom_arrondissement_communes::varchar as commune,
    capacity::int as total_capacity,
    numbikesavailable::int as bikes_available,
    numdocksavailable::int as docks_available,
    mechanical::int as mechanical_bikes,
    ebike::int as electric_bikes,
    case when is_installed = 'OUI' then true else false end as is_installed,
    case when is_renting = 'OUI' then true else false end as is_renting,
    case when is_returning = 'OUI' then true else false end as is_returning,
    duedate::timestamp as last_updated_at
from public.raw_velib