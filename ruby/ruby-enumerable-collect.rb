# https://www.hackerrank.com/challenges/ruby-enumerable-collect
# Enter your code here. Read input from STDIN. Print output to STDOUT

def rot13(secret_messages)
  secret_messages.collect {|char| char.tr 'A-Za-z','N-ZA-Mn-za-m'}
end


