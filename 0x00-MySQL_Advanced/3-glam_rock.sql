-- a SQL script that lists all bands with Glam rock
-- as their main style, ranked by their longevity
SELECT band_name, (2022 - formed) AS lifespan FROM WHERE split IS NULL metal_bands ORDER BY lifespan DESC;
