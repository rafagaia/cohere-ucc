import sys
import cohere


class CohereService:
    def __init__(self, api_key, model_size,seq, arr_prompts):
        self.api_key = api_key
        self.model_size = model_size
        self.seq = seq
        self.prompts = arr_prompts
        self.co = None
        # self.co = connect()
        # self.colinkSequence()

    def connect(self):
        self.co = cohere.Client(self.api_key)
        return self.co
        

    # links one request to another, or back to same one.
    # setFlowSequence([('pc',1), ('pg',1000), ('pc',1)])
    #   Classifies once +=> generates twice => classifies once
    def colinkSequence(self):
      # create file here, and open it.
        transform_words = ""
        for tupl in self.seq:
            for prompt in self.prompts:
                transform_words+=prompt + "||||||"
          # access fd (file descriptor)
          # shouldn't the condition be tupl[1] == tupl[1] - 1
            cycles = tupl[1]
            while (cycles > 0):
                print(f'\n****Cycles {cycles}***')
                cycles -=1
              # open file here
                if tupl[0] == 'pg':
                    transform_words+=self.__performGenerate(
                        transform_words)
                  # @TODO write to file
                  # close file
                elif tupl[0] == 'pc':
                  transform_words+=self.__performClassify(
                    transform_words,
                    (context_prompt + user_prompt))
                    # @TODO write to file
                    # close file
                else:
                    continue
        return transform_words

    def __performClassify(self,i,ex):
        if not (self.co):
            print('[Unauthorized] You must first connect to Cohere API.')
            return 0
        else:
            response = self.co.classify(
                model=self.model_size,
                inputs=i,
                examples=ex
            )
            print('Classification: {}'.format(response.classifications))
            return response.classifications


    def __performGenerate(self, p):
        if not self.co:
            print('[Unauthorized] You must first connect to Cohere API.')
            return 0
        else:
            response = self.co.generate(prompt=p)
            print('Prediction: {}'.format(response.generations[0].text))
            return response.generations[0].text




  # @TODO: graphSequence
      
      # graphSequence
    # def graphSequence(context_prompt, user_prompt, seq):    


def cohere_start(api_key, model_size, seq, arr_prompts):
    print("\n********** new process *************\n")
    co = CohereService(api_key, model_size, seq, arr_prompts)
    co.connect()
    result = co.colinkSequence()
    print(f'Response Result: {result}')
    sys.exit(0)
    #@TODO: persist result to local file, or write to Database.