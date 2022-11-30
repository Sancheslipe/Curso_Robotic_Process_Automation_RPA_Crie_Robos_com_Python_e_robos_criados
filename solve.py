from solveRecaptcha import solveRecaptcha
# fazendo o captcha
print('carregando captcha')
result = solveRecaptcha(
"6LcMmBcdAAAAAKU3pJ3PSl-20-mf1wDYpvMJGe1T",
"https://www.cpqd.com.br/teste-captcha/";
)

code = result['code']

print(code)

EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))

driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")

p.sleep(1)