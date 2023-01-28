import cohere

# @TODO: do we need modules? how to properly export CohereService?

class CohereService:
    def __init__(self, api_key, model_size, service):
        self.api_key = api_key
        self.model_size = model_size
        self.service = 'generate' # 'classify', 'embed'

    def connect():
        self.co = cohere.Client(self.api_key)

    # links one request to another, or back to same one.
    # setFlowSequence([('pc',1), ('pg',2), ('pc',1)])
    #   Classifies once +=> generates twice => classifies once
    def linkedSequence(context_prompt, user_prompt, seq):
        transform_words = context_prompt+"\n"+user_prompt
      # create file here, and open it.
        for tupl in seq:
          # access fd (file descriptor)
            while ((tupl[1] = tupl[1] - 1)):
              # open file here
                if tupl[0] == 'pg':
                    transform_words+=__performGenerate(
                        transform_words)
                  # @TODO write to file
                  # close file
                elif tupl[0] == 'pc':
                  transform_words+=__performClassify(
                    self.model_size,
                    transform_words,
                    (context_prompt + user_prompt))
                    # @TODO write to file
                    # close file
                else:
                    continue
        return transform_words

      # @TODO: graphSequence
      #     


    def __performClassify(m,i,ex):
        if not self.co:
            print('[Unauthorized] You must first connect to Cohere API.')
            return 0
        else:
            response = self.co.classify(
                model=m,
                inputs=i,
                examples=ex
            )
            print('Classification: {}'.format(response.classifications))
            return response.classifications


    def __performGenerate(p):
        if not self.co:
            print('[Unauthorized] You must first connect to Cohere API.')
            return 0
        else:
            response = self.co.generate(prompt=p)
            print('Prediction: {}'.format(response.generations[0].text))
            return response.generations[0].text





    