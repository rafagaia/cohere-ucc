import cohere

class CohereService:
    def __init__(self, api_key, service):
        self.api_key = api_key
        self.service = service # 'generate' or 'classify' or 'embed'

    def connect(API_KEY):
        self.co = cohere.Client(self.api_key)

    # links one request to another, or back to same one.
    # setFlowSequence([('pc',1), ('pg',2), ('pc',1)])
    #   Classifies once +=> generates twice => classifies once
    def linkedSequence(context_prompt, user_prompt, seq):
        transform_words = context_prompt + user_prompt
        for tupl in seq:
            while (tupl[1] = tupl[1] - 1):
                if tupl[0] == 'pg':
                    transform_words+=__performGenerate(
                        transform_words)
                elif tupl[0] == 'pc':
                    transform_words+=__performClassify(
                        'small',
                        transform_words,
                        (context_prompt + user_prompt))
                else:
                    continue
        return transform_words


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
            return response


    def __performGenerate(p):
        if not self.co:
            print('[Unauthorized] You must first connect to Cohere API.')
            return 0
        else:
            response = self.co.generate(prompt=p)
            print('Prediction: {}'.format(response.generations[0].text))
            return response





    