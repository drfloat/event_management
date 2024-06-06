{# Welcome this module was created by pranav salunkhe
    "name": "Event Management",
    "summary": "Add event management",
    "version": "1.0",
    "application": True,
    "installable": True,
    "author": "pranav",
    "website": "https://www.pranav.net",
    "license":"LGPL-3",
    "depends" : ["base",'mail'],
    #here is a index and description of each xml or csv file that created
    "data": [
        "views/event_event_view.xml",# 1.model for creating events
        "views/event_attendee_view.xml",# 2.model for creating attendees
        "views/event_organizer_view.xml",# 3.model for creating organisers
        "views/event_registeration_view.xml",# 4.model for registering
        "views/menu_views.xml", # 5. keeps track of all the menus created
        "security/ir.model.access.csv", # 6. security file for the module
        "security/security.xml", #7. keeps track of all the groups and their rules
        "wizards/registeration_report_wizard_views.xml", #8. view for wizard
        "data/email_templates.xml", #9. email template
    ]
    # Welcome this module was created by pranav salunkhe
}