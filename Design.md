# RendezView Design Document

This document is for high level design discuessions for this application.

## Organiser Logic

- Need an account (Email & Password)
- Choose RendezView type 
    - Trip - Days
    - Event - Days & Times
- Name your RendezView
- Choose the date / time ranges
- Can set a bunch of optional filters too
    - Exclude certains days - Weekdays
    - Exclude certain times - Working hours
    - Set a limit to the amount of attendees
- Click finish and a shareable link will be created
- Then you add your name and availability to the RendezView (Maybe this should happen before generating the link...?)


## Attendee Logic

- Don't need an account 
- Enter your name
- Enter your availability (Choose dates and times)


## Who this could be aimed at

- Social media
    - Help groups of friends organise holidays/trips/events 
    - Could integrate with Skyscanner/Airbnb/Trivago to show you best flights/accomadation available for those dates

- Professional
    - Organising work trips/large meetings
    - Could be a useful roster making tool for managers with part time / fluctuating staff

- Sports teams
    - Could be useful for organising training and matches 
    - Could integrate with Spond