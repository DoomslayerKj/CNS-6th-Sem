#Factorisation Attack

from factordb.factordb import FactorDB
from Crypto.Util.number import inverse

def factors(a):
	f=FactorDB(a)
	f.get_factor_list()
	f.connect()
	f.get_factor_list()
	return f.get_factor_list()

if __name__=='__main__':




	n=71641831546926719303369645296528546480083425905458247405279061196214424558100678947996271179659761521775290973790597533683668081173314940392098256721488468660504161994357
	# n= x*y , x and y being large prime numbers


	e = 65537 
	#the integer co-prime of totient

	#c = cipher
	c = 63127079832500412362950100242549738176318170072331491750802716138621322974529994914407846448954487685068331564008936808539420562251661435790855422130443584773306161128156

	####### question ends here
	print("\nIntercepted Data = N(modulus),E,C(cipher)\n")
	print(f"N(modulus) = {n}  ")

	print(f"\nE = {e}\n")
	print(f"C = {c}")


	print("\n\n\nCalculating Factors....")
	
	p=factors(n)[0]
	q=factors(n)[1]

	phi = (p-1)*(q-1)


	d=inverse(e,phi) 


	m = pow(c,d,n)
	
	print(f"\nFactors from N:")
	print(f"\nP={p}\nQ={q}\n")
	print("...Cracking RSA...\n\n\n")

	print(f"Totient(phi) = {phi}\n")
	print(f"D = {d}\n")

	print(f"Decoded Message = {m}\n ")

	hex_String=hex(m)[2:]

	print(f"Hex String = {hex_String} \n")

	bytes_object = bytes.fromhex(hex_String)

	ascii_string = bytes_object.decode("ASCII")

	print(f"Decrypted Plain Text: {ascii_string}")
