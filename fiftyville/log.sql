-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Getting the crime scene reports from Humphrey Street on July 28, 2021.
SELECT *
FROM crime_scene_reports
WHERE street = 'Humphrey Street' AND year = 2021 AND month = 7 AND day = 28;

-- Checking ATM transactions on and after the day of the theft.
SELECT *
FROM atm_transactions
WHERE (year = 2021 AND month = 7 AND day >= 28)
ORDER BY year, month, day;

-- Checking phone calls on the day of the theft.
SELECT *
FROM phone_calls
WHERE (year = 2021 AND month = 7 AND day = 28)
ORDER BY duration DESC;

-- Finding flights that departed shortly after the theft.
SELECT flights.*, airports.city
FROM flights
JOIN airports ON flights.destination_airport_id = airports.id
WHERE (year = 2021 AND month = 7 AND day >= 28)
ORDER BY year, month, day, hour, minute;

-- Reviewing interview transcripts for any suspicious information.
SELECT *
FROM interviews
WHERE year = 2021 AND month = 7 AND day >= 28;

-- Cross-referencing to find common names in atm transactions and phone calls.
SELECT atm_transactions.account_number, phone_calls.caller, phone_calls.receiver
FROM atm_transactions, phone_calls
WHERE atm_transactions.year = phone_calls.year AND atm_transactions.month = phone_calls.month AND atm_transactions.day = phone_calls.day
AND ((atm_transactions.year = 2021 AND atm_transactions.month = 7 AND atm_transactions.day >= 28));

-- Finding people who had both ATM transactions and phone calls on the day of the theft or shortly after.
SELECT atm.account_number, pc.caller, pc.receiver
FROM atm_transactions AS atm, phone_calls AS pc
WHERE atm.year = pc.year AND atm.month = pc.month AND atm.day = pc.day
AND (atm.year = 2021 AND atm.month = 7 AND atm.day >= 28);

-- Identify potential suspects:
SELECT *
FROM atm_transactions
WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Humphrey Street';

SELECT *
FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND (caller IN (list_of_account_numbers) OR receiver IN (list_of_account_numbers));

-- Interview Witnesses:
SELECT name, transcript
FROM interviews
WHERE year = 2021 AND month = 7 AND day >= 28;

-- If you have suspects, you can narrow down searches to specific individuals.
SELECT *
FROM interviews
WHERE name = 'Suspect Name';