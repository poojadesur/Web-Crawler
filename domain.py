from urllib.parse import urlparse


# get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-3] + '.' + results[-2] + '.' + results[-1]
    except:
        print('Error')
        return ''



# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        # print(urlparse(url).netloc)
        return urlparse(url).netloc
    except:
        print('error')
        return ''

# print(get_domain_name('https://www.learnamic.com/resource_providers/the-new-boston'))
# print(get_domain_name('https://web.iiit.ac.in/~pooja.desur/index.html'))
# print(get_sub_domain_name('https://web.iiit.ac.in/~pooja.desur/index.html'))

