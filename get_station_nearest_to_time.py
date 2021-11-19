from datetime import datetime
import pandas

def get_nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))


def get_station_nearest_to_time(query_time, station_filename="data/BB3_time_log_09_2019.csv"):
    """
    This returns the station for the given dt.
    Picks the station based on known station visit times in STATION_TIMES.
    
    Station returned should:
    * have cast start time before query_time (with some tolerance)
    
    """    
    # array of stations and known dts (from spreadsheet)
    with open(station_filename) as station_file:
        station_df = pandas.read_csv(
            station_file,
            parse_dates = {'dt':["DATE", "INITIAL TIME (UTC)"]}  # this should parse the two columns together as one datetime
        )
    
    # convert datetime column to type datetime[ns], will convert non-match to NaT
    station_df['dt']= pandas.to_datetime(
        station_df['dt'], 
        errors = 'coerce',
        exact = True
    ) 
    
    station_df = station_df.dropna(how='all')  
    
    timestamp = get_nearest(station_df['dt'], query_time)
    return station_df.query(f"dt == '{timestamp}'").iloc[0]

#     # === get the time closest to but not less than query_time
#     closest_s_t = station_df["dt"][0]  # start with the first row of dataframe
#     closest_s_t_index = 0 
#     # iterate through all STATION_TIMES, keeping track only of the current closest one
#     # for each row... NOTE: not sure if will loop through rows or columns for dataframe
#     for s_t_i, s_t in enumerate(station_df["dt"]):  
#         # if current s_t is closer to query_time than our current s_t 
#         # print(f"{s_t_i} : {s_t}")
#         if s_t - query_time < closest_s_t - query_time:  # NOTE: do we need to abs() here?
#             closest_s_t = s_t  # set 
#             closest_s_t_index = s_t_i
#     return station_df.loc[closest_s_t_index]  # return the row

