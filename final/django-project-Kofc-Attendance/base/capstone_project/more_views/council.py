from ..models import User, Council, Event, Analytics, Donation, blockchain, ForumCategory, ForumMessage, Notification, EventAttendance, Recruitment
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.db.models import Max
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def manage_councils(request):
    """View for managing councils - add or remove"""
    if request.user.role != 'admin':
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('dashboard')
    
    councils = Council.objects.all().order_by('name')
    
    # Get member count for each council
    council_data = []
    for council in councils:
        member_count = User.objects.filter(council=council, is_archived=False).count()
        council_data.append({
            'council': council,
            'member_count': member_count
        })
    
    context = {
        'council_data': council_data,
    }
    
    return render(request, 'manage_councils.html', context)

@login_required
@require_http_methods(["POST"])
def add_council(request):
    """Add a new council"""
    if request.user.role != 'admin':
        messages.error(request, 'You do not have permission to perform this action.')
        return redirect('dashboard')
    
    council_name = request.POST.get('council_name', '').strip()
    location_street = request.POST.get('location_street', '').strip()
    location_barangay = request.POST.get('location_barangay', '').strip()
    location_city = request.POST.get('location_city', '').strip()
    location_province = request.POST.get('location_province', '').strip()
    location_zip_code = request.POST.get('location_zip_code', '').strip()
    
    if not council_name:
        messages.error(request, 'Council name is required.')
        return redirect('manage_councils')
    
    # Check if council already exists
    if Council.objects.filter(name__iexact=council_name).exists():
        messages.error(request, f'Council "{council_name}" already exists.')
        return redirect('manage_councils')
    
    # Create the council
    Council.objects.create(
        name=council_name,
        district='',
        location_street=location_street,
        location_barangay=location_barangay,
        location_city=location_city,
        location_province=location_province,
        location_zip_code=location_zip_code
    )
    
    messages.success(request, f'Council "{council_name}" has been added successfully.')
    return redirect('manage_councils')

@login_required
@require_http_methods(["POST"])
def delete_council(request, council_id):
    """Delete a council"""
    if request.user.role != 'admin':
        messages.error(request, 'You do not have permission to perform this action.')
        return redirect('dashboard')
    
    try:
        council = Council.objects.get(id=council_id)
        
        # Check if council has members
        member_count = User.objects.filter(council=council, is_archived=False).count()
        if member_count > 0:
            messages.error(request, f'Cannot delete council "{council.name}" because it has {member_count} active member(s). Please reassign members first.')
            return redirect('manage_councils')
        
        council_name = council.name
        council.delete()
        messages.success(request, f'Council "{council_name}" has been deleted successfully.')
    except Council.DoesNotExist:
        messages.error(request, 'Council not found.')
    except Exception as e:
        messages.error(request, f'Error deleting council: {str(e)}')
    
    return redirect('manage_councils')

@login_required
@require_http_methods(["POST"])
def edit_council(request, council_id):
    """Edit a council's information"""
    if request.user.role != 'admin':
        messages.error(request, 'You do not have permission to perform this action.')
        return redirect('dashboard')
    
    try:
        council = Council.objects.get(id=council_id)
        council_name = request.POST.get('council_name', '').strip()
        location_street = request.POST.get('location_street', '').strip()
        location_barangay = request.POST.get('location_barangay', '').strip()
        location_city = request.POST.get('location_city', '').strip()
        location_province = request.POST.get('location_province', '').strip()
        location_zip_code = request.POST.get('location_zip_code', '').strip()
        
        if not council_name:
            messages.error(request, 'Council name is required.')
            return redirect('manage_councils')
        
        # Check if another council with the same name exists
        if Council.objects.filter(name__iexact=council_name).exclude(id=council_id).exists():
            messages.error(request, f'Another council with the name "{council_name}" already exists.')
            return redirect('manage_councils')
        
        # Just update the existing council
        council.name = council_name
        council.location_street = location_street
        council.location_barangay = location_barangay
        council.location_city = location_city
        council.location_province = location_province
        council.location_zip_code = location_zip_code
        council.save()
        
        messages.success(request, f'Council "{council_name}" has been updated successfully.')
    except Council.DoesNotExist:
        messages.error(request, 'Council not found.')
    except Exception as e:
        messages.error(request, f'Error updating council: {str(e)}')
    
    return redirect('manage_councils')

