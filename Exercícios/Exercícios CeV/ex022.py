x = str(input("Digite seu nome completo: ")).strip()
print(f"Seu nome em maiúsculas é {x.upper()}."
      f"\nSeu nome em minúsculas é {x.lower()}."
      f"\nSeu nome tem {len(x)-x.count(' ')} letras."
      f"\nSeu primeiro nome é {x.split()[0]} e tem {len(x.split()[0])} letras.")
