from django.urls import path
from capstone_project import views
from capstone_project.more_views import api_endpoints, council

urlpatterns = [
    path('', views.capstone_project, name='capstone_project'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pending-users/', views.manage_pending_users, name='manage_pending_users'),
    path('approve-user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('reject-user/<int:user_id>/', views.reject_user, name='reject_user'),
    path('promote-user/<int:user_id>/', views.promote_user, name='promote_user'),
    path('demote-user/<int:user_id>/', views.demote_user, name='demote_user'),
    path('archive-user/<int:user_id>/', views.archive_user, name='archive_user'),
    path('analytics-form/', views.analytics_form, name='analytics_form'),
    path('analytics-view/', views.analytics_view, name='analytics_view'),
    path('archived-users/', views.archived_users, name='archived_users'),
    path('mission_vision/', views.mission_vision, name='mission_vision'),
    path('faith-action/', views.faith_action, name='faith-action'),
    path('councils/', views.councils, name='councils'),
    path('council/<int:council_id>/', views.council_detail, name='council_detail'),
    path('donations/', views.donations, name='donations'),
    path('about_us/', views.about_us, name='about_us'),
    path('events-management/', views.events_management, name='events_management'),
    path('donation-reports/', views.donation_reports, name='donation_reports'),
    path('manual_donation/', views.manual_donation, name='manual_donation'),
    path('review_manual_donations/', views.review_manual_donations, name='review_manual_donations'),
    path('gcash/initiate', views.initiate_gcash_payment, name='initiate_gcash_payment'),
    path('success/', views.success_page, name='success_page'),
    path('cancel/', views.cancel_page, name='cancel_page'),
    path('gcash/confirm/', views.confirm_gcash_payment, name='confirm_gcash_payment'),
    path('blockchain/', views.get_blockchain_data, name='blockchain'),
    path('blockchain/receipt/request/<str:transaction_id>/', views.request_receipt, name='request_receipt'),
    path('blockchain/receipt/download/<str:transaction_id>/', views.download_receipt, name='download_receipt'),
    path('blockchain/receipt/send/<str:transaction_id>/', views.send_receipt, name='send_receipt'),
    # path('search-users/', views.search_users, name='search_users'),

    # New endpoint for recruiter name autocomplete
    path('search-members/', views.search_members, name='search_members'),

    # Username and email validation endpoints
    path('check-username/', views.check_username, name='check_username'),
    path('check-email/', views.check_email, name='check_email'),

    path('forum/', views.forum, name='forum'),
    path('forum/messages/<int:category_id>/', views.get_messages, name='get_messages'),
    path('forum/send/', views.send_message, name='send_message'),
    path('forum/delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('forum/pin/<int:message_id>/', views.pin_message, name='pin_message'),

    # URLs for role management and events
    path('manage-roles/', views.manage_roles, name='manage_roles'),
    path('add-event/', views.add_event, name='add_event'),
    path('edit-event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('event-proposals/', views.event_proposals, name='event_proposals'),
    path('approve-event/<int:event_id>/', views.approve_event, name='approve_event'),
    path('reject-event/<int:event_id>/', views.reject_event, name='reject_event'),
    path('event/<int:event_id>/details/', views.event_details, name='event_details'),
    path('archived-events/', views.archived_events, name='archived_events'),

    # New URLs for member and event lists
    path('event-list/', views.event_list, name='event_list'),
    path('member-list/', views.member_list, name='member_list'),
    path('council-members/', views.council_members, name='council_members'),
    path('council-events/', views.council_events, name='council_events'),
    path('update-degree/<int:user_id>/', views.update_degree, name='update_degree'),

    # User details endpoint
    path('user/<int:user_id>/details/', views.user_details, name='user_details'),

    # Event attendance management
    path('event/<int:event_id>/attendance/', views.event_attendance, name='event_attendance'),
    path('event/update-attendance/', views.update_attendance, name='update_attendance'),

    # Member activities
    path('member-activities/', views.member_activities, name='member_activities'),

    # My Recruits
    path('my-recruits/', views.my_recruits, name='my_recruits'),

    # Add Recruitment Record
    path('add-recruitment/', views.add_recruitment, name='add_recruitment'),

    # Undo Recruitment Change
    path('undo-recruitment/<int:history_id>/', views.undo_recruitment, name='undo_recruitment'),

    # Change Council
    path('change-council/<int:user_id>/', views.change_council, name='change_council'),

    # Leaderboard
    path('leaderboard/', views.leaderboard, name='leaderboard'),

    # Notifications
    path('notifications/', views.notifications_list, name='notifications'),
    path('notifications/count/', views.notifications_count, name='notifications_count'),
    path('notifications/mark-read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),
    path('notifications/mark-all-read/', views.mark_all_notifications_read, name='mark_all_notifications_read'),

    # Council Management (NEW)
    path('manage-councils/', council.manage_councils, name='manage_councils'),
    path('add-council/', council.add_council, name='add_council'),
    path('delete-council/<int:council_id>/', council.delete_council, name='delete_council'),
    path('edit-council/<int:council_id>/', council.edit_council, name='edit_council'),

    # API Endpoints (NEW)
    path('api/event-counts/', api_endpoints.event_counts_api, name='event_counts_api'),
    path('api/council-event-counts/', api_endpoints.council_event_counts_api, name='council_event_counts_api'),
    path('api/user-counts/', api_endpoints.user_counts_api, name='user_counts_api'),
    path('api/council-user-counts/', api_endpoints.council_user_counts_api, name='council_user_counts_api'),
    path('api/event/<int:event_id>/download-data/', api_endpoints.event_download_data, name='event_download_data'),
]

