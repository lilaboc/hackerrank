# https://www.hackerrank.com/challenges/ruby-hash-method-each
# Enter your code here. Read input from STDIN. Print output to STDOUT
def iter_hash(hash)
    hash.each do |key, value|
      puts key
      puts value
    end
end
