-- Modèle Marts enrichi : Métriques métier et indicateurs d'alerte
with staging as (
    select * from {{ ref('stg_velib') }}
)

select
    station_id,
    station_name,
    commune,
    total_capacity,
    bikes_available,
    docks_available,
    mechanical_bikes,
    electric_bikes,

    -- 1. Taux de disponibilité global (%)
    case 
        when total_capacity > 0 
        then round((bikes_available::numeric / total_capacity::numeric) * 100, 2)
        else 0 
    end as availability_rate_pct,

    -- 2. Taux d'électrification de la flotte disponible (%)
    case 
        when bikes_available > 0 
        then round((electric_bikes::numeric / bikes_available::numeric) * 100, 2)
        else 0 
    end as electrification_rate_pct,

    -- 3. Statut opérationnel de la station (Alerte logistique)
    case 
        when bikes_available = 0 then 'Rupture'
        when docks_available = 0 then 'Saturée'
        else 'Nominale'
    end as station_status,

    is_installed,
    is_renting,
    is_returning,
    last_updated_at
from staging