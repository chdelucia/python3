import dns
import dns.resolver

answers = dns.resolver.resolve('dnspython.org', 'MX')
for rdata in answers:
    print('Host', rdata.exchange, 'has preference', rdata.preference)


# A IPV4
# AAAA IPV6
# NS NameServer
# MX MailServer
ansA = dns.resolver.resolve('google.com', 'A')

# Para debugear que tiene el objeto
# print(ansA)

ansMX = dns.resolver.resolve('google.com', 'MX')
ansNS = dns.resolver.resolve('google.com', 'NS')
ansAAAA = dns.resolver.resolve('google.com', 'AAAA')

print(ansA.response.to_text())

