SELECT name, area, population -- Select the name, area, and population of countries
FROM World -- From the World table
WHERE area >= 3000000 OR population >= 25000000  -- Filter for big countries, such as those with an area of at least 3 million square kilometers or a population of at least 25 million people