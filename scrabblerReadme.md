The program solves the following problems:-

1. What words from the dictionary the user can spell with these letters?
2. What words begin with these letters as a prefix?
3. What words end with these letters as a suffix?

Given is a word dictionary file "words.txt"

For 1st problem type := scrabbler "Any number of letters" 
                        eg: scarbbler abcdefg
                        
For 2nd problem type := scrabbler --prefix "Any number of letters" 
                        eg: scarbbler -prefix car

For 3rd problem type := scrabbler --suffix "Any number of letters" 
                        eg: scarbbler ing

For all the above problems solution will be printed on console in alpabetically sored order


Performance Optimization:-

    I have used 'Trie' data structure for indexing the given dictionary.
    I have used Trie for solving all the above given problems.
    But I have used on more data structre which is a vector of dictionary inside dictionary.
            eg:  { a : { 2 : ['ad', 'an' , 'as' ...] }
                       { 3 : ['ash' , 'act' , add' ...] }
                       { 4 : ['abbe' , 'abed' , 'abet' ...]}
                         :
                         :
                   b : { 2 : ['be' , 'by' ] }
                       { 3 : ['baa' , 'bad' , 'bag' ...] }
                         :
                         :
                   :
                   :
                   z : { ................. }
                     :
                 }
      
    This data structure is used for searching when user gives input of mare than 7 letters.
    Analysis of the program shows for maximum 7 different letters the total number of possible words without repeating letters is 5040.
    These 5040 words can be searched in Trie datastructure efficiently in optimized time.
    But when user enters 8 different unique letters the possible number of words become 40320 which is too many words to be searched in Trie.
    In above such cases we used vectored datastructure for performance optimization as even in the worse case scenario the number of searches wold not exceed the size of
    dictionary. This datastructure helps reduce the search space first by seaching only those words which starts with the given letters.
    And secondly searching only those words whose length is not more than the given letters.                               
