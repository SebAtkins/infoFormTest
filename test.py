import openai

openai.api_key = "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"

# prompt = "Return a comma separated list of the information required for a contract to sell a house from a 50 house development."

# completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

# answers = completion.choices[0].message.content

# print(answers)
# print("===")

def getFields():
    answers = "1. Property address\n2. Seller's name and contact information\n3. Buyer's name and contact information\n4. Purchase price of the house\n5. Earnest money deposit amount\n6. Closing date\n7. Property description\n8. Home inspection contingency\n9. Financing terms (if applicable)\n10. Disclosure of any known property defects or issues\n11. Warranty details (if applicable)\n12. Escrow instructions\n13. Title and deed related information\n14. Special provisions or conditions\n15. Closing costs allocation\n16. Timeframe for response and acceptance of the offer\n17. Contingencies such as sale of buyer's current home\n18. Dispute resolution terms\n19. Signatures of both parties\n20. Additional terms specific to the development (if applicable)\n\nNote: This list is not exhaustive and may vary depending on the specific requirements and legalities in your jurisdiction. It is always advisable to consult with a real estate attorney or professional to ensure all necessary information is included in the contract."

    prompt = "Return a comma separated list of the information required for a contract to sell a house from a 50 house development."

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

    answers = completion.choices[0].message.content

    # Put all lines into a dict
    line = ""
    info = []
    for i in answers:
        if i != "\n":
            line += i
        else:
            info.append(line)
            line = ""

    # Select only lines starting with a number (gets needed fields)

    fields = []
    for i in info:
        if len(i) > 0:
            if i[0].isnumeric():
                fields.append(i)

    #print(fields)

    return fields