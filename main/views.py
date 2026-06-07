from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import FileResponse
from django.views.decorators.http import require_http_methods
from .models import Resume
from .forms import ResumeUploadForm

def home(request):
    techs = [
        'Python', 'Django', 'REST API', 'React', 'JavaScript', 'SQL',
        'Flask', 'TCP/IP', 'AWS', 'Linux', 'Git', 'Wireshark',
        'Cisco Packet Tracer', 'Django ORM', 'Bootstrap',
    ]
    return render(request, 'main/home.html', {'techs': techs})

def about(request):
    certs = [
        {'icon': '🐍', 'name': 'Python Programming Certification'},
        {'icon': '🌐', 'name': 'Django Full Stack Development'},
        {'icon': '🗄️', 'name': 'SQL / Database Management'},
        {'icon': '☁️', 'name': 'AWS Cloud Fundamentals'},
    ]
    return render(request, 'main/about.html', {'certs': certs})

def skills(request):
    fullstack_skills = [
        {'name': 'Python', 'level': 90, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg'},
        {'name': 'Django', 'level': 85, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg'},
        {'name': 'REST APIs', 'level': 82, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg'},
        {'name': 'JavaScript', 'level': 70, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg'},
        {'name': 'React', 'level': 65, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg'},
        {'name': 'Flask', 'level': 75, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg'},
        {'name': 'SQL', 'level': 80, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg'},
        {'name': 'HTML5', 'level': 88, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg'},
        {'name': 'CSS3', 'level': 82, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg'},
        {'name': 'Bootstrap', 'level': 78, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg'},
    ]
    networking_skills = [
        {'name': 'TCP/IP', 'level': 80, 'img': 'https://img.icons8.com/color/96/network.png'},
        {'name': 'OSI Model', 'level': 78, 'img': 'https://img.icons8.com/color/96/layers.png'},
        {'name': 'DNS & DHCP', 'level': 75, 'img': 'https://img.icons8.com/color/96/domain.png'},
        {'name': 'VLANs', 'level': 72, 'img': 'https://img.icons8.com/color/96/switch.png'},
        {'name': 'OSPF / RIP', 'level': 65, 'img': 'https://img.icons8.com/color/96/router.png'},
        {'name': 'HTTP/HTTPS', 'level': 85, 'img': 'https://img.icons8.com/color/96/https.png'},
        {'name': 'Subnetting', 'level': 75, 'img': 'https://img.icons8.com/color/96/subnet-mask.png'},
        {'name': 'Firewalls / VPN', 'level': 65, 'img': 'https://img.icons8.com/color/96/firewall.png'},
    ]
    tools_skills = [
        {'name': 'Git & GitHub', 'level': 85, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg'},
        {'name': 'Linux', 'level': 75, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg'},
        {'name': 'AWS', 'level': 60, 'img': 'https://img.icons8.com/color/96/amazon-web-services.png'},
        {'name': 'Wireshark', 'level': 72, 'img': 'https://img.icons8.com/color/96/wireshark.png'},
        {'name': 'Cisco Packet Tracer', 'level': 75, 'img': 'https://img.icons8.com/color/96/cisco.png'},
        {'name': 'Windows Server', 'level': 65, 'img': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/windows8/windows8-original.svg'},
    ]
    return render(request, 'main/skills.html', {
        'fullstack_skills': fullstack_skills,
        'networking_skills': networking_skills,
        'tools_skills': tools_skills,
    })

def projects(request):
    projects = [
        {
            'icon': '📈',
            'title': 'Online Trading & Portfolio Management System',
            'desc': 'A comprehensive backend system for online trading with real-time portfolio tracking, built with Django and optimised SQL queries.',
            'points': [
                'Designed and developed RESTful APIs using Django REST Framework',
                'Managed user transactions, buy/sell order flows, and live portfolio data',
                'Optimised complex SQL queries for performance under high data loads',
                'Implemented secure JWT authentication and session handling',
            ],
            'tags': ['Python', 'Django', 'REST API', 'SQL', 'JWT'],
            'img': 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=600&auto=format&fit=crop',
        },
        {
            'icon': '🎓',
            'title': 'Student Management System (Django)',
            'desc': 'A Django-based CRUD application for managing student records with automated workflows and clean admin interface.',
            'points': [
                'Built full CRUD operations using Django ORM and class-based views',
                'Automated academic record management with a clean admin dashboard',
                'Implemented search, filter, and pagination for large datasets',
                'Designed responsive UI using Bootstrap and Django templating engine',
            ],
            'tags': ['Python', 'Django', 'ORM', 'CRUD', 'Bootstrap'],
            'img': 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=600&auto=format&fit=crop',
        },
        {
            'icon': '🌐',
            'title': 'Network Simulation Lab (Cisco Packet Tracer)',
            'desc': 'Designed and configured multi-topology enterprise networks in Cisco Packet Tracer with full routing, VLANs, and troubleshooting.',
            'points': [
                'Designed LAN/WAN topologies including star, mesh, and hybrid layouts',
                'Configured IP addressing schemes, subnetting, and inter-VLAN routing',
                'Set up OSPF and RIP routing protocols across multiple routers',
                'Performed systematic network troubleshooting using ping, traceroute, and Wireshark',
            ],
            'tags': ['Cisco Packet Tracer', 'OSPF', 'VLANs', 'TCP/IP', 'Wireshark'],
            'img': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop',
        },
    ]
    return render(request, 'main/projects.html', {'projects': projects})


def hire_me(request):
    from pathlib import Path
    resume_path = Path(r"C:\Users\RUSHI\Downloads\Resume_python.pdf")
    resume_exists = resume_path.exists()
    
    return render(request, 'main/hire_me.html', {
        'resume_exists': resume_exists,
        'resume_filename': 'Resume_python.pdf',
    })


@require_http_methods(["GET"])
def download_resume(request):
    from pathlib import Path
    
    resume_path = Path(r"C:\Users\RUSHI\Downloads\Resume_python.pdf")
    
    if not resume_path.exists():
        messages.error(request, 'Resume file not found.')
        return redirect('hire_me')
    
    try:
        file = resume_path.open('rb')
        response = FileResponse(file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{resume_path.name}"'
        return response
    except Exception as e:
        messages.error(request, f'Error downloading resume: {str(e)}')
        return redirect('hire_me')


def contact(request):
    from .forms import ContactForm
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']
            email = form.cleaned_data['email']
            phone = form.cleaned_data.get('phone', '')
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            job_type = form.cleaned_data['job_type']
            
            # Send email
            from django.core.mail import send_mail
            email_body = f"""
New Message from Your Portfolio:

Name: {name}
Company: {company}
Email: {email}
Phone: {phone}
Job Type: {job_type}

Subject: {subject}

Message:
{message}
            """
            
            try:
                send_mail(
                    f'Portfolio Contact: {subject}',
                    email_body,
                    'your-email@gmail.com',
                    ['rautrushikesh003@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, '✅ Message sent successfully! I\'ll get back to you soon.')
                return redirect('contact')
            except Exception as e:
                messages.error(request, f'❌ Error sending message. Please try again.')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})

