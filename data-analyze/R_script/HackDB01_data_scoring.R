# Load libraries
library(dplyr)
library(mongolite)
library(lubridate)


# setup connection for drivers/drivers profile
con <- mongo(collection = "DriversTrucks",
             db = "HackDB01",
             url = "mongodb://localhost",
             verbose = FALSE)

driverstrucks <- con$find(query = '{}', field = '{}')

#setup connection for goods
con <- mongo(collection = "Goods",
             db = "HackDB01",
             url = "mongodb://localhost",
             verbose = FALSE)

goods <- con$find(query = '{}', field = '{}')

# Merge dataset left on goods
df <- goods %>%
  left_join(driverstrucks, by = c("t_id" = "_id")) %>%
  mutate(timestamp_calc = Sys.time(),
         g_pickdate = ymd_hms(g_pickdate),
         g_delivdate = ymd_hms(g_delivdate),
         g_movement = as.logical(g_movement),
         rest_score = if_else(g_movement == TRUE, 5, -2),
         totaldays = as.numeric(difftime(g_delivdate, g_pickdate) / (60 * 60 *24)),
         time_score = as.numeric(cut(totaldays,
                          breaks = c(-Inf, 2, 4, 6, Inf),
                          labels=c(0, 0.5, 1, 1.75))),
         accident_score = if_else(g_accident == "alcohol", -3,
                                  if_else(g_accident == "sleep", -2,
                                          if_else(g_accident == "external", -1, 3))),
         violation_score = if_else(g_num_violations == "drug", -3,
                                   if_else(g_num_violations == "emergency", -1.5,
                                           if_else(g_num_violations == "line", -0.5,
                                                   if_else(g_num_violations == "speed", -1, 2)))),
         t_maxload = as.numeric(t_maxload),
         g_weight = as.numeric(g_weight),
         load_score = if_else(g_weight > t_maxload, -2, 0),
         truck_age = as.numeric(difftime(timestamp_calc, t_issuedate) / 24),
         total_score = rest_score + time_score + accident_score + violation_score + load_score,
         safety_score = total_score / max(total_score),
         safety_category = cut(safety_score,
                               breaks = c(-Inf, -0.20, 0.12, 0.35, Inf),
                               labels = c("Danger", "Caution", "Reliable", "Trustworthy"))) %>%
  group_by(t_id) %>%
  summarize(nbr_trip = n(),
            avg_rest = sum(g_movement) / n(),
            nbr_days_drive = sum(totaldays),
            total_dist_drive = sum(g_dist),
            max_dist = max(g_dist),
            avg_daily_dist = sum(g_dist) / (sum(totaldays) + 1),
            nbr_accident = sum(g_accident != "CLEAR"),
            nbr_truck_maintenance = sum(g_incident != "CLEAR"),
            nbr_violations = sum(g_num_violations != "CLEAR"),
            truck_age = max(truck_age),
            truck_reg_date = max(t_regdate),
            latest_tyre_change = max(g_pickdate[which(g_incident == "tyre")]),
            avg_safety_score = mean(safety_score, na.rm = TRUE),
            avg_weight = mean(g_weight, na.rm = TRUE),
            max_weight = max(g_weight)) %>%
  mutate(latest_tyre_change = ymd_hms(latest_tyre_change),
         latest_tyre_change = if_else(is.na(latest_tyre_change),
                                      ymd_hms(truck_reg_date), latest_tyre_change),
         tyre_unchanged_time = as.numeric(difftime(Sys.time(), latest_tyre_change) / 24),
         maintenance_score = if_else(tyre_unchanged_time > 365, 0, 1),
         avg_daily_score = if_else(avg_daily_dist < 1000, 1, 0),
         accident_score = if_else(nbr_accident / nbr_trip > 0.05, 0, 1),
         mileage_score = if_else(total_dist_drive / truck_age * 365 > 300000, 0, 1),
         truck_score = (maintenance_score + avg_daily_score + accident_score + mileage_score) / 4)

