#!/usr/bin/env ruby
# Function Definition
def show(name)
  #msg = "Good morning, " + name
  #res = "Good Night #{name}"
  "Hello #{name}"
  #return res
end

a = "Hello, world!"
4.times { puts a }

# With/without parenthesis
puts show "Grillo"
puts show ("Humberto")

a = a.split(/,+\s|!+/)
# Iterators
a.each { |word| puts word }

print "in-line"
puts " -> a ver"

# Input
print "insert your name: " 
line = gets "\n"
print line

puts("REGX in Ruby")
m = "School bro como school estos".scan(/School/i)
puts m[0]
puts m[1]
