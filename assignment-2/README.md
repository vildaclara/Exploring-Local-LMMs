# Assignment 2 – Trustworthy AI Engineering

## Reflections on our test results

We ran all five tests ten times, and every test passed, giving us a test pass rate of 100%. At first, this seemed like a very good result, but we decided to add CSV logging so that we could save the actual responses and look at them more closely. When going through these responses, we had some interesting findings.

We could clearly see the non-deterministic nature of LLMs. Even though we used the same model and the same prompt several times, we received different responses. Our results show that the model always included the correct capital of both Sweden and Australia in our logs, so even though the responses vary, the model was still consistent enough and provided what was expected (the capital).

## Hallucinations and response quality

When going through our responses, we certainly found some examples of hallucinations. What we found interesting was that the model gave us the correct capital but then continued to provide incorrect information.

For example, in some responses, the model claimed that Australia has two capitals and that Canberra is a city-state. Another interesting example was the following response:

> The capital of Australia is Canberra.
>
> It’s interesting because it's a self-governing territory and has never officially been named as the capital. It was established as the seat of government in 1908.

We found it interesting that the model actually contradicts itself in one and the same answer. It starts by telling us that Canberra is the capital of Australia, but then goes on to say that it has never officially been named as the capital. So even though the model is consistent in giving us the correct capital across different responses, it is not necessarily consistent within the same response.

We also found a response where Stockholm was described as officially being known as the “City of a Thousand Islands”. This was not a name we recognised, and we couldn't find anything online to confirm this either.

Another thing we reflected on was the usability of some of the responses. For example:

> The capital of Sweden is Stockholm.
>
> It’s a bit of a tricky question – Stockholm is a major city, but it’s also the country’s capital.

There is nothing incorrect about Stockholm being both a major city and the capital of Sweden, but in what way is this a tricky question? We felt that this response could actually confuse the user more than it helps them. Although we would not necessarily call this a hallucination, it is an interesting example of how a response can be factually correct without necessarily being useful or clear.

There were also several examples of more subjective responses, where Stockholm was described as a “wonderfully unique city”, or a “very famous and important city”. These are not necessarily hallucinations either, but we can question how relevant this information is to the user.

Something that all these examples have in common is that the model provides additional information that we did not ask for which seems to increase the risk of providing incorrect or confusing information. We could potentially reduce this risk with clearer prompts, for example by asking the model to only respond with the name of the capital.

## Limitations

Our results made us question whether checking for the presence of the correct capital in the responses is a sufficient property check. In several cases, the correct capital was included, but we still consider the response incorrect because of other parts of the response.

Our consistency tests only require two out of three responses to pass the property check. It would be interesting to experiment with a threshold of 100% to see how often individual responses fail the property check. With the current testing, the model could give us an incorrect capital in one response without us necessarily noticing it if we had not implemented logging. But even with a stricter threshold, our current property check would still not detect the hallucinations we found, which shows us that a pass rate of 100% ≠ factual accuracy.

## LLM-as-a-Judge

We used Gemma 3 (gemma3:1b) as our generator and Llama 3.2 (llama3.2:latest) as our judge. We tested the judge by giving it two predefined answers where we expected it to accept "The capital of Sweden is Stockholm" and reject "The capital of Bealandia is Bea City" (Bealandia being a made-up country). Both tests passed in every run.

This means that we only use LLM-as-a-Judge in two out of five tests, and not in our consistency tests. We are testing the generator and the judge separately. It would be interesting to see if the judge could detect the hallucinations that our property checks missed. Since the judge itself is also an AI that can make mistakes, we would still want to manually review the responses to understand if a mistake was made and by whom - the generator or the judge.

## Further reflections

Our results also made us reflect on the quality of our tests. Having five tests does not necessarily mean that an AI component has been thoroughly tested. What matters is whether the tests cover different types of errors. In our case, the consistency tests only check whether the correct capital appears in the response, leaving additional incorrect information undetected.

We also think that independent verification is important when evaluating AI-generated answers. An LLM used as a judge can make mistakes just like the model being evaluated. Comparing answers against independently verified reference data could therefore provide a more reliable way of checking factual accuracy.

Finally, we noticed that the model often added information that was not requested. A more restrictive prompt, asking for only the capital’s name, might reduce unnecessary details and the risk of introducing incorrect information. However, this would need to be tested before we could determine whether it actually improves reliability.
