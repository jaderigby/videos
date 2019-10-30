import messages as msg

# settings = helpers.get_settings()

def execute():
    movieName = raw_input("What's the name of your movie? ")
    print '''
<video preload="none" poster="/staticcontent/serovital.com/videos/posters/{movie}.jpg" controls="">
    <source src="/staticcontent/serovital.com/videos/{movie}.mp4" type="video/mp4">
    <source src="/staticcontent/serovital.com/videos/{movie}.webm" type="video/webm">
    <p>Your browser does not support the HTML5 Video element.</p>
</video>
'''.format(movie=movieName)
