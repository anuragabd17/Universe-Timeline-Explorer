
double cosmic_calendar_day(double universe_age,
                           double event_age) {

    if (universe_age <= 0 ||
        event_age < 0 ||
        event_age > universe_age) {
        return -1.0;
    }

    double day = ((universe_age - event_age)
                  / universe_age) * 365.0;

    return day;
}
