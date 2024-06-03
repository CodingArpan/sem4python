from django.http import HttpResponse


def home_page(request):
    return HttpResponse('''
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <div class="text-center">
        <img src="https://media.licdn.com/dms/image/D4D03AQFrYXMQ1Hxo4w/profile-displayphoto-shrink_800_800/0/1706633848722?e=1721865600&amp;v=beta&amp;t=WRVH20UiRHv_rV_IYM6XE83M4qB-kks-LX3r7Vm1CeM" alt="Profile Picture" class="rounded-full mx-auto mb-4 w-60 h-60">
        <h1 class="text-2xl font-bold mb-2">John Doe</h1>
        <p class="text-gray-700">A passionate developer with over 1 years of experience in software development. </p>
    </div>
</body>
''')
