import pandas as pd
import sqlite3

# =========================
# Database Connections
# =========================

##### Part I: Basic Filtering #####

# Connect to each database
# conn1: planets.db
conn1 = sqlite3.connect('planets.db')

# conn2: dogs.db
conn2 = sqlite3.connect('dogs.db')

# conn3: babe_ruth.db
conn3 = sqlite3.connect('babe_ruth.db')

# =========================
# Part 1: Basic Filtering
# =========================

# STEP 0 (reference) – view full table
# pd.read_sql("""SELECT * FROM planets; """, conn1)

# STEP 1
# Return all the columns for planets that have 0 moons.
# WHERE moons = 0
# The result is stored in df_no_moons so tests can inspect it.
df_no_moons = pd.read_sql(
    """
    SELECT *
    FROM planets
    WHERE num_of_moons = 0;
    """,
    conn1
)

# STEP 2
# Return the name and mass of each planet that has a name with exactly 7 letters.
# We use LENGTH(name) = 7 instead of hard-coding the names.
df_name_seven = pd.read_sql(
    """
    SELECT name, mass
    FROM planets
    WHERE LENGTH(name) = 7;
    """,
    conn1
)

# =========================
# Part 2: Advanced Filtering
# =========================

# STEP 3
# Return the name and mass for each planet that has a mass that is less than or equal to 1.00.
df_mass = pd.read_sql(
    """
    SELECT name, mass
    FROM planets
    WHERE mass <= 1.00;
    """,
    conn1
)

# STEP 4
# Return all the columns for planets that have at least one moon and a mass less than 1.00.
df_mass_moon = pd.read_sql(
    """
    SELECT *
    FROM planets
    WHERE num_of_moons >= 1
      AND mass < 1.00;
    """,
    conn1
)

# STEP 5
# Return the name and color of planets that have a color containing the string "blue".
# Use LIKE with wildcard matching.
df_blue = pd.read_sql(
    """
    SELECT name, color
    FROM planets
    WHERE color LIKE '%blue%';
    """,
    conn1
)

# =========================
# Part 3: Ordering and Limiting
# =========================

# STEP 0 (reference) – view full table
# pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6
# Return the name, age, and breed of all dogs that are hungry (hungry = 1)
# Sort them from youngest to oldest (age ASC).
df_hungry = pd.read_sql(
    """
    SELECT name, age, breed
    FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC;
    """,
    conn2
)

# STEP 7
# Return the name, age, and hungry columns for hungry dogs between the ages of two and seven (inclusive).
# Sort these dogs alphabetically by name.
df_hungry_ages = pd.read_sql(
    """
    SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1
      AND age BETWEEN 2 AND 7
    ORDER BY name ASC;
    """,
    conn2
)

# STEP 8
# Return the name, age, and breed for the 4 oldest dogs.
df_4_oldest = pd.read_sql(
    """
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC
    LIMIT 4;
    """,
    conn2
)

# =========================
# Part 4: Aggregation
# =========================

# STEP 0 (reference) – view full table
# pd.read_sql("""
# SELECT * FROM babe_ruth_stats; """, conn3)

# STEP 9
# Return the total number of years that Babe Ruth played professional baseball.
# We'll count distinct years.
df_ruth_years = pd.read_sql(
    """
    SELECT COUNT(DISTINCT year) AS total_years
    FROM babe_ruth_stats;
    """,
    conn3
)

# STEP 10
# Return the total number of home runs hit by Babe Ruth during his career.
# Sum the season home run column.
df_hr_total = pd.read_sql(
    """
    SELECT SUM(HR) AS total_home_runs
    FROM babe_ruth_stats;
    """,
    conn3
)

# =========================
# Part 5: Grouping and Aggregation
# =========================

# STEP 11
# For each team that Babe Ruth has played on, return the team name and
# the number of years he played on that team, aliased as number_years.
df_teams_years = pd.read_sql(
    """
    SELECT team,
           COUNT(DISTINCT year) AS number_years
    FROM babe_ruth_stats
    GROUP BY team;
    """,
    conn3
)

# STEP 12
# For each team that Babe Ruth played on and averaged over 200 at-bats with,
# return the team name and average number of at-bats, aliased as average_at_bats.
# We use HAVING to filter based on the aggregate AVG(at_bats).
df_at_bats = pd.read_sql(
    """
    SELECT team,
           AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    HAVING AVG(at_bats) > 200;
    """,
    conn3
)

conn1.close()
conn2.close()
conn3.close()