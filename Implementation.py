#Import the required Libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as fnt
from langdetect import detect
from mahaNLP.similarity import SimilarityAnalyzer


import nltk
from nltk import word_tokenize
nltk.download("punkt")
import random
import pyiwn
iwn = pyiwn.IndoWordNet(lang=pyiwn.Language.MARATHI)
# Loads the default model- marathi-sentence-similarity-sbert
similarity_model = SimilarityAnalyzer() 
print("Similarity Analyzer loaded")
#######################################################
#######################################################
#######################################################

win = Tk()
win.geometry("1530x790")

#Define the PhotoImage Constructor by passing the image file
img= PhotoImage(file='mountain.png', master= win)
img_label= Label(win,image=img)

#define the position of the image
img_label.pack()



title_lbl = Label(text="Anvayartha", font=("times new roman", 35, "bold","italic"), bg="#0A8F98", fg="white")
title_lbl.place(x=0, y=0, width=1530, height=100)

main_frame = LabelFrame(win, bd=5, bg="white", relief=RIDGE,text="Paraphrase", font=20)
main_frame.place(x=150, y=110, width=1200, height=600)


img_main= PhotoImage(file='a.png', master= main_frame)
img_main_label= Label(main_frame,image=img_main)
img_main_label.pack()


ip_name = Label(main_frame,fg='white' ,text = "Input",font=("times new roman", 20, "bold"),bg='#0A8F98', borderwidth=2,relief="groove")
ip_name.place(x=40, y=50)


ip_entry=Text(main_frame, width = 80, height = 50, wrap = WORD,font=10, borderwidth=2)
ip_entry.place(x=250, y=20,height=150)


op_name = Label(main_frame,fg='white' ,text = "Output",font=("times new roman", 20, "bold"),bg='#0A8F98', borderwidth=2,relief="groove")
op_name.place(x=40, y=400)

op_box = Text(main_frame,font=10,wrap = WORD, borderwidth=2)
op_box.place(x=250,y=260,height=300,width=900)
#op_box.pack()
'''
list_i=list()
def paraphrase_fun_call(ip_string):
    list_i.append(ip_string)
    list_p=['राम , एक आदर्श शासक , प्रकांड योद्धा व सहिष्णू राजा होते .', 'राम , एक आदर्श शासक , महान योद्धा व सोशिक राजा होते .']
   
    list_i.append( 'राम , एक आदर्श शासक , प्रकांड योद्धा व सहिष्णू ')
    for day in list_i:
        op_box.insert(END, day + '\n')


'''
def paraphrase_Input():
   ip_string= ip_entry.get(1.0, "end-1c")
   print(ip_string)
   validate_input(ip_string)
  
   

#Create a Button to validate Entry Widget
submit_btn=Button(main_frame, text= "Submit",font = fnt.Font(size = 15),width= 20,height=1, command=paraphrase_Input,bg='#0A8F98',activebackground='blue',fg='white')
submit_btn.place(x=550,y=200)

#win.mainloop()

#################################################################
#################################################################
def validate_input(input_string):
    lang=detect(input_string)
    if lang == 'mr':
        paraphrase_fun_call(input_string)
    else:
        op_box.delete("1.0","end")
        op = "Please enter input sentence in Marathi"
        op_box.insert(END, op + '\n') 
        

def paraphrase_fun_call(sent_inp):
   

    #sent_inp=input('Enter marathi sentence you want to paraphrase')
    end_idx=len(sent_inp)-1
    op_box.delete("1.0","end")
  
    #Tokenization
    words = word_tokenize(sent_inp)
    print("After Tokenization!")
    print(words)
    
    
    #punctuation removal
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    words_without_punc=list()
    for word in words:
      if word not in punctuations:
        words_without_punc.append(word)
    print("After Punctuation Removal!")
    print(words_without_punc)
    
    
    #stop word removal
    mr_stop_words='"अशी","असलयाचे","असलेल्या","असेल","आपले","असायला","आम्हांला","असल्यामुळे",असा","असते","असून","असे","आज","आणि","आता","आपल्या","असतो","आला","आपल्याकडे",कोणत्याही","काहीजण",आली","आले","यांचे","आमचे","आहे","आहेत","एका","कमी","करणयात","करून","का","करता","काम","काय","करतात","आल्या","तिच्या","तुझे","तुझीच","त्यासाठी","तुझ्यापुढे","तिची","तुमच्या","काही","किवा","की","केला","केली","होतेच","केले","गेल्या","घेऊन","जात","जेव्हा","तुम्ही","झाला","झाली","झाले","झालेल्या","टा","डॉ","तू","तर","तरी","तिचे","तिला","तसेच","ता","ती","तीन","ते","तो","त्या","तेव्हा","त्याचा","त्याची","त्याच्या","त्याना","तेथे","त्यानी","त्यामुळे","त्री","दिली","न","नाही","पण","म","माझे","माझा","माझ्या","मात्र","मी","मिळवता","परंतु","म्हणतात","म्हणजे","म्हणाले","म्हणून","येथून","या","याचा","याची","याच्या","याना","जो","यानी","होतो","येणार","येत","येथील","येथे","व","हा","ही","होणारच","हे","होणार","होत","होता","होती","होते" '
    words_without_stopwords=list()
    for word in words_without_punc:
      if word not in mr_stop_words:
        words_without_stopwords.append(word)
    print("After Stop Words Removal!")
    print(words_without_stopwords)
    
    
    
    
    ##############################################################
    
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
    # categorizing words in input to its part of speech
    import codecs
    import re
    from functools import reduce
    
    keywords_adjective=list()
    keywords_adverb=list()
    keywords_noun=list()
    keywords_verb=list()
    
    
    suffix_adjective={}
    suffix_adverb={}
    suffix_noun={}
    suffix_verb={}
    
    word_root={}
    word_suff={}
    
    synset_list=list()
    
    
    
    class Tokenizer():
      '''class for tokenizer'''
    
      def __init__(self,text=None):
        text=str(text)
        if text is  not None:
          self.text=text.encode('utf-8')
          #print(self.text)
        else:
          self.text=None
        self.sentences=[]
        self.tokens=[]
        self.stemmed_word=[]
        self.final_list=[]
        #self.final_tokens=[]
    
      def remove_only_space_words(self):
        tokens_dec=[]
        tokens_enc=[]
    
        for each in self.tokens:
          tokens_dec.append(each.decode('utf-8'))
        tokens=filter(lambda tok: tok.strip(),tokens_dec)
    
        for each in tokens_dec:
          tokens_enc.append(each.encode('utf-8'))
        self.tokens=tokens_enc
        
        
      def hyphenated_tokens(self):
        for each in self.tokens:
          if '-'.encode('utf-8') in each:
            tok=each.split('-'.encode('utf-8'))
            self.tokens.remove(each)
            self.tokens.append(tok[0])
            self.tokens.append(tok[1])
    
      def generate_sentences(self):
        '''generates a list of sentences'''
        text=self.text
        self.sentences=text.split("।".encode())
    
      def print_sentences(self,sentences=None):
        print("====",sentences)
        if sentences:
          for i in sentences:
            print("<<<<<<",i.decode('utf-8'))
        else:
          for i in self.sentences:
            print(">>>>>",i.decode('utf-8'))
    
    
    
      def tokenize(self):
        '''done'''
        if not self.sentences:
          self.generate_sentences()
    
        sentences_list=self.sentences
        tokens=[]
        for each in sentences_list:
          word_list=each.split(' '.encode('utf-8'))
          tokens=tokens+word_list
        self.tokens=tokens
        #remove words containing spaces
        self.remove_only_space_words()
        #remove hyphenated words
        self.hyphenated_tokens()
        #remove hyphenated words
    
      def print_tokens(self,print_list=None):
        
        if print_list is None:
          for i in filter(None,self.tokens):
            print("***",i.decode('utf-8'))
        
        else:
          for i in print_list:
            print(i.encode('utf-8'))
    
    
      def tokens_count(self):
        '''done'''
        return len(self.tokens)
    
      def sentence_count(self):
        '''done'''
        return len(self.sentences)
    
      def len_text(self):
        '''done'''
        return len(self.text)
        
      def print_freq_dict(self,freq):
        '''done'''
        for i in freq.keys():
          #print(i,"(((((")
          print(i.decode('utf-8'),',',freq[i])
    
      def generate_stem_words(self,word_dec):
        word=word_dec.encode('utf-8')
        suffixes_mar = {
        1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा",u"च"],
        2: [u"च्या",u"न्या",u"न्या",u"ही",u"नी",u"ल्या",u"चा",u"ाचे",u"ची",u"ाने",u"ता"],
        3: [u"पण",u"सुद्धा",u"कडे",u"पाशी",u"हून",u"तून",u"मुळे",u"वर",u"तील",u"नीही",u"मध्ये",u"याची",u"पण",u"तेचा", u"ीच्या"],
        4: [u"प्रमाणे",u"ावर",u"ासाठी",u"पासून",u"कडून",u"वरून",u"कडेही",u"मधले",u"मधल"]
        
      }
        for L in 4, 3, 2, 1:
          if len(word) > L + 1:
            for suf in suffixes_mar[L]:
              if word_dec.endswith(suf):
                print(word_dec," -> ",word_dec[:-len(suf)]," -> ",suf)
                word_dec=word_dec[:-len(suf)]
                if isInIndo(word_dec):
                    return word_dec
                #return word_dec[:-len(suf)]
            
            
        return word_dec
    
      def generate_stem_dict(self):
        '''returns a dictionary of stem words for each token'''
    
        stem_word={}
        if not self.tokens:
          self.tokenize()
        for each_token in self.tokens:
          #print type(each_token)
          temp=self.generate_stem_words(each_token.decode('utf-8'))
          #print temp
          stem_word[each_token]=temp
          self.stemmed_word.append(temp)
          
        return stem_word
    
    
    
    
    def placeInPOSList(w,suff,mainword):
      pos_name=iwn.synsets(w)[0].pos()
      print (w, ":", pos_name)
      word_root[w]=mainword
      word_suff[mainword]=suff
      if(pos_name=='adjective' and w not in keywords_adjective):
          keywords_adjective.append(w)
          suffix_adjective[w]=suff
    
      else:
        if(pos_name=='noun'and w not in keywords_noun):
          keywords_noun.append(w)
          suffix_noun[w]=suff
        else:
          if(pos_name=='verb'and w not in keywords_verb):
            keywords_verb.append(w)
            suffix_verb[w]=suff
          else:
            if(pos_name=='adverb'and w not in keywords_adverb):
                keywords_adverb.append(w)
                suffix_adverb[w]=suff
    
    def isInIndo(w):
      if iwn.synsets(w):
        return True
      return False
    
    #words_without_stopwords=['कागाळीची']
    
    
    for w in words_without_stopwords:
            currentword=w
            previousW=""
            if isInIndo(w):
              placeInPOSList(w,"",w)
              
            else:
              while not isInIndo(currentword) and currentword!=previousW :
                t=Tokenizer(currentword)
                t.tokenize()
                #f=t.generate_freq_dict()
                f=t.generate_stem_words(currentword)
                print("hh",f)
                previousW=currentword
                currentword=f
                print("ppp ",currentword,previousW)
              if isInIndo(currentword):
                res = reduce(lambda s, sub: s.replace(sub, ""), currentword, w)
                placeInPOSList(currentword,res,w)
                
              
    
    
              
                
    print("\n")
    print('adjective',keywords_adjective)
    print('adverb',keywords_adverb)
    print('noun',keywords_noun)
    print('verb',keywords_verb)
    
                
    print("\n")
    print('suff adjective',suffix_adjective)
    print('suff adverb',suffix_adverb)
    print('suff noun',suffix_noun)
    print('suff verb',suffix_verb)
    
    print(word_root)
        
    ###################################################
    
    
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
    #path to csv ngram folder
        
    
    # importing the module
    import json
    import os
    import csv
    gram_path="C:/reena/Ngram"
    
    os.chdir(gram_path)
    
    unigramKeyVal={}
    bigramKeyVal={}
    trigramKeyVal={}
    
    def getTrigramKeyList():
      file="trigram.csv"
      gramfile_path=f"{gram_path}/{file}"
     
      with open(gramfile_path, 'r', encoding='utf8') as csvfile:
              firstLine=True
              csvreader= csv.reader(csvfile)
              for line in csvreader:
                if line and firstLine==False:
                  trigramKeyVal[line[0]]=line[1]
                firstLine=False
      return trigramKeyVal
    
    
    def getBigramKeyList():
      file="bigram.csv"
      gramfile_path=f"{gram_path}/{file}"
     
      with open(gramfile_path, 'r' , encoding='utf8') as csvfile:
              firstLine=True
              csvreader= csv.reader(csvfile)
              for line in csvreader:
                if line and firstLine==False:
                  bigramKeyVal[line[0]]=line[1]
                firstLine=False
      return bigramKeyVal
    
    
    def getUnigramKeyList():
    
      file="unigram.csv"
      gramfile_path=f"{gram_path}/{file}"
     
      with open(gramfile_path, 'r' , encoding='utf8') as csvfile:
              firstLine=True
              csvreader= csv.reader(csvfile)
              for line in csvreader:
                if line and firstLine==False:
                  unigramKeyVal[line[0]]=line[1]
                firstLine=False
      return unigramKeyVal
    
    storeBigramInUse={}
    storeTrigramInUse={}
    def isProperWord(stemandsuffword,stemword,ipwords,idx):
      if stemandsuffword in getUnigramKeyList():
        return stemandsuffword
      else:
        # reading the data from the file
        with open("C:/reena/Ngram/stemmed.txt" , encoding='utf8') as f:
          data = f.read()
        js = json.loads(data)
        if stemword in js:
          currentwordsuffixes=js[stemword]
          bigramlist=getBigramKeyList()
          actualword=""
          actualwordcount=0
          for eachsuffix in currentwordsuffixes:
            bigramtocheck=eachsuffix+" "+ipwords[idx+1]
            if bigramtocheck in bigramlist:
              if int(bigramlist[bigramtocheck]) > int(actualwordcount):
                actualword=eachsuffix
                actualwordcount=bigramlist[bigramtocheck]
                storeBigramInUse[actualword]=actualwordcount
          if actualword!="" :
            if len(storeBigramInUse)>1:
              max_value = max(storeBigramInUse.values())
              for key,value in storeBigramInUse.items():
                if value == max_value:
                    storeTrigramInUse[key]=value
    
              trigramlist=getTrigramKeyList()
              actualTriword=""
              actualTriwordcount=0
              trigramToCheck=""
              for key,value in storeTrigramInUse.items():
                if idx-1>=0:
                  trigramToCheck=ipwords[idx-1]+" "+key
                  if idx+1<len(ipwords):
                    trigramToCheck=trigramToCheck+" "+ipwords[idx+1]
                if trigramToCheck!="":
                  #print(trigramlist[trigramToCheck])
                  if int(trigramlist[trigramToCheck])>int(actualTriwordcount):               
                    actualTriword=key
                    actualwordcount=trigramlist[trigramToCheck]
    
              if actualTriword!="":
                actualword=actualTriword
    
            return actualword
          else:
            return False
        
    # selection of candidate words
    # priority is ->  adjective > noun > verb > adverb
    
    
    pos1=''
    
    if(len(keywords_adjective)>0):
      keywords=keywords_adjective
      pos1='adjective'
    else:
        if(len(keywords_noun)>0):
          keywords=keywords_noun
          pos1='noun'
        else:
          if(len(keywords_verb)>0):
            keywords=keywords_verb
            pos1='verb'
          else:
              if(len(keywords_adverb)>0):
                keywords=keywords_adverb
                pos1='adverb'
      
    print(keywords)
    
    
    i=1
    all_synonyms=[]
    selected_from_replaced={}
    op_lists_paraphrased=list()
    while i<=len(keywords):
      while len(selected_from_replaced)!=i:
        keyword=random.choice(keywords)
        if selected_from_replaced.get(keyword) is None :  
          
          all_synsets = iwn.synsets(keyword)
          all_synonymstemp=[]
          all_synonyms=[]
          for synset in all_synsets:
                all_synonymstemp.append(synset.lemma_names())
          for symset in all_synonymstemp:
            for word in symset:
              all_synonyms.append(word)
          replaced_word=random.choice(all_synonyms)
    
          if(len(all_synonyms)==1 and all_synonyms[0]==keyword ):
              break
          else:
              trial=1
              while(keyword==replaced_word) and trial<6:
                    replaced_word=random.choice(all_synonyms)
                    trial=trial+1
    
          root_word=word_root[keyword]
          selected_from_replaced[root_word]=replaced_word
       
      
      #generating the output based on tokenised words
    
      op_words=list()
      idx=0
    
      for p in words:
            #if current word is the candidate word, replace it with synonyms
    
        if selected_from_replaced.get(p) is not None :
          if word_suff[p]=="" or isProperWord(selected_from_replaced.get(p)+word_suff[p],selected_from_replaced.get(p),words,idx)!=False :
            if word_suff[p]=="":
              finalword=selected_from_replaced.get(p)
            else:
              finalword=isProperWord(selected_from_replaced.get(p)+word_suff[p],selected_from_replaced.get(p),words,idx)
            op_words.append(finalword)
        else:
          op_words.append(p)
        idx=idx+1
            
       #Paraphrased sentence words
      selected_from_replaced={}
      
      paraphrased_sentence= ' '.join([str(elem) for elem in op_words])
      #store paraphrased sentences
      op_lists_paraphrased.append(paraphrased_sentence)
      i=i+1
    
    
    print(op_lists_paraphrased)


########################################################3

    j=0
    similarity_score=similarity_model.get_similarity_score(sent_inp,op_lists_paraphrased)
    for op in op_lists_paraphrased:
        sentence2=op
        print("sentence1"+ sent_inp)
        print("sentence 2" + sentence2)
        print(similarity_score[j])
        op_box.insert(END, op + " , " + str(similarity_score[j]) + '\n')
        j=j+1

    print(similarity_model.get_similarity_score(sent_inp,op_lists_paraphrased))

win.mainloop()


