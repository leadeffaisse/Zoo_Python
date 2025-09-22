from dataclasses import dataclass, field


@dataclass
class Contact:
    phone: str
    email: str

    def __str__(self):
        return f'{self.phone}/{self.email}'

@dataclass
class Address:
    address: str
    postal_code: str
    city: str

    def __str__(self):
        return f"{self.address}, ({self.postal_code}) {self.city}"

@dataclass
class Personne:
    last_name: str
    first_name: str
    birth_date: str
    contact: Contact
    address: Address

    full_name: str = field(init=False)

    def __post_init__(self):
        self.full_name = f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.full_name} : {self.contact}"

@dataclass
class Repertoire:
    contacts: list[Personne] = field(default_factory=list)

    def add_contact(self, personne: Personne):
        self.contacts.append(personne)

    def __str__(self):
        if not self.contacts:
            return "Répertoire vide."
        result = "Répertoire :\n"
        for personne in self.contacts:
            result += f"  {personne}\n"
        return result.rstrip()


if __name__ == "__main__":
    contact1 = Contact("0649785322", "jacquesdupont@gmail.com")
    address1 = Address("65 rue des champs", "26400", "Crest")
    personne1 = Personne("Dupont", "Jacques", "03/08/1970", contact1, address1)

    contact2 = Contact("0649785322", "jeandupond@gmail.com")
    address2 = Address("0649785322", "26400", "Crest")
    personne2 = Personne("Dupond", "Jean", "03/04/1996", contact2, address2)

    repertoire1 = Repertoire()
    repertoire1.add_contact(personne1)
    repertoire1.add_contact(personne2)

    print(repertoire1)