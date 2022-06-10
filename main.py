class Vulnerability:
    output = []

    def __init__(self, name, description, rank=0):
        self.name = name
        self.description = description
        self.rank = rank
        self.output.append(f'NAME ----> {self.name} ')

    def list_of_vulnerabilities(self):
        j = 1
        for insecurity in self.output:
            print(f'№ {j}, ' + insecurity)
            j += 1

    def comparison_of_vulnerabilities(self, other):
        if self.rank - other.rank > 0:
            print(f"rank {self.name} > rank {other.name} ----> {self.name} more dangerous")

        elif self.rank - other.rank < 0:
            print(f"rank {other.name} > rank {self.name} ----> {other.name} more dangerous")

        else:
            print(f"rank {other.name} = rank {self.name} ----> danger is equal")

    def upper(self, num):
        self.rank += num

    def lower(self, num):
        self.rank -= num


Clickjacking = Vulnerability('Clickjacking', 'Attacker uses multiple transparent or opaque layers to trick a user into'
                                             ' clicking on a button or link on another page when they were intending '
                                             'to click on the top level page. Thus, the attacker is “hijacking” clicks'
                                             ' meant for their page and routing them to another page, most likely owned'
                                             ' by another application, domain, or both.', 999)

Insecure_design = Vulnerability('Insecure design',
                                'Insecure design is a broad category representing different weaknesses,'
                                ' expressed as “missing or ineffective control design.” One of the '
                                'factors that contribute to insecure design is the lack of business risk'
                                ' profiling inherent in the software or system being developed, and thus'
                                ' the failure to determine what level of security design is required.', 5)

Insecure_design.list_of_vulnerabilities()
Insecure_design.comparison_of_vulnerabilities(Clickjacking)

Clickjacking.lower(998)
Insecure_design.comparison_of_vulnerabilities(Clickjacking)
