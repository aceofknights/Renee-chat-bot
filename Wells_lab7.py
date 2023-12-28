import random
import string


def checkEmotion(text):
    common_emotions = ['happy', 'sad', 'angry', 'excited',  'fearful', 'surprised', 'relaxed']

    found_emotion = None

    words = text.lower().split()  # Convert the text to lowercase and split it into words

    for word in words:
        if word in common_emotions:
            found_emotion = word
            break  # Exit the loop as soon as a common emotion is found

    return found_emotion

# seperating emotions so positve responses wont be giving for negative prompts
positive_emotions = ['happy', 'joyful', 'excited', 'content', 'grateful', 'peaceful', 'enthusiastic']
negative_emotions = ['sad', 'angry', 'anxious', 'fearful', 'disappointed', 'guilty', 'lonely', 'frustrated', 'scared']
family_members = ['mother', 'mom', 'father', 'dad', 'uncle', 'aunt', 'sister', 'brother', 'grandmother', 'grandfather']


def getReply(line, words):
  
  emotion = checkEmotion(line)

  if len(words) == 0:
    response = random.choice([
        "Ummm... like... Helloooooo?",
        "Hey there! Say something.",
        "What's on your mind?",
        "Hello! How can I assist you today?",
        "Don't be shy! I'm here to help.",
    ])
    return response

  if line[-1] == '?':
    response = random.choice([
        "Why do you ask?",
        "Great question! What's on your mind?",
        "I'm curious about your question. Can you tell me more?",
        "Hmm, that's an interesting inquiry. Please share more details.",
        "Questions are always welcome! How can I assist you?",
    ])
    return response

  for member in family_members:
        if member in words:
            response = random.choice([
                f"Tell me more about your {member}.",
                f"What's your favorite memory with your {member}?",
                f"How has your relationship with your {member} been?",
            ])
            return response
        
  if 'you are great' in words or 'you are awesome' in words:
    response = random.choice([
        "Thank you for the compliment!",
        "I'm just a program, but I appreciate the kind words.",
    ])
    return response

  if 'thank you' in words or 'thanks' in words:
    response = random.choice([
        "You're welcome! I'm here to help.",
        "No problem, happy to assist!",
    ])
    return response

  if 'hobby' in words or 'interest' in words:
    response = random.choice([
        "Tell me more about your hobbies or interests. What do you enjoy doing in your free time?",
        "I'm curious about your hobbies. What's something you're passionate about?",
    ])
    return response

  if 'creative' in words or 'artistic' in words:
    response = random.choice([
        "Creativity can be a powerful outlet for self-expression. How do you like to express your creativity?",
        "Exploring your artistic side can be fulfilling. Tell me more about your creative pursuits.",
    ])
    return response

  if 'stress relief' in words or 'relaxation' in words:
    response = random.choice([
        "Engaging in hobbies is an excellent way to relieve stress and find relaxation. How does your hobby help you unwind?",
        "Hobbies are great for promoting relaxation. Can you share how your hobby brings peace to your life?",
    ])
    return response

  if 'try something new' in words or 'explore new interests' in words:
    response = random.choice([
        "Exploring new hobbies can be an exciting journey. Is there something specific you'd like to try or learn?",
        "Trying new activities can be a great way to expand your interests. What's something you've been curious to explore?",
    ])
    return response

  if 'stay engaged' in words or 'keep busy' in words:
    response = random.choice([
        "Hobbies can help you stay engaged and fulfilled. How do your interests keep you motivated and active?",
        "Staying busy with your hobbies is a positive way to engage with life. What's the most fulfilling aspect of your hobbies for you?",
    ])
    return response

  if 'weather' in words:
    response = random.choice([
        "I'm not a weather expert, but I can help you find the weather forecast for your location.",
        "Do you want to know the weather for a specific location?",
    ])
    return response

  if 'not sure' in words or 'confused' in words:
    response = random.choice([
        "That's okay! It's normal to be unsure sometimes. Can I help clarify anything for you?",
        "If you have any questions, feel free to ask, and I'll do my best to provide answers.",
    ])
    return response

  if 'exciting' in words:
    response = random.choice([
        "I can sense your excitement! What's making you feel so excited?",
        "That's wonderful! Tell me more about what's exciting you right now.",
    ])
    return response
  
  if 'understand myself' in words or 'self-discovery' in words:
    response = random.choice([
        "Self-discovery is a journey. What aspects of yourself would you like to explore further?",
        "Understanding yourself is a valuable process. What insights are you hoping to gain on this journey?",
    ])
    return response

  if 'problem' in words or 'challenge' in words:
    response = random.choice([
        "Let's work together to find possible solutions to the challenges you're facing.",
        "Problem-solving can be empowering. Can you describe the specific issue you'd like to address?",
    ])
    return response

  if 'emotional support' in words or 'talk to someone' in words:
    response = random.choice([
        "I'm here to provide emotional support. What's been weighing on your mind?",
        "You're not alone. I'm here to lend a listening ear. How can I assist you today?",
    ])
    return response

  if 'progress' in words or 'improvement' in words:
    response = random.choice([
        "It's important to acknowledge your progress. What positive changes have you noticed recently?",
        "Every step forward is a step in the right direction. What achievements are you proud of?",
    ])
    return response

  if 'not listening' in words or 'ignored' in words:
    response = random.choice([
        "I'm here to listen, and I value what you have to say. I'm sorry if it seems otherwise. Please share your thoughts, and I'll do my best to be attentive.",
        "I'm truly listening, and your feelings matter. If you feel unheard, let's talk about how I can better support you.",
    ])
    return response

  if 'communication' in words or 'express' in words:
    response = random.choice([
        "Effective communication is vital in our conversation. How can I make you feel more heard and understood?",
        "Your feedback is valuable. Let's discuss how we can improve our communication and make this a more positive experience for you.",
    ])
    return response

  if 'killed' in line:
    response = random.choice([
        "I'm truly sorry to hear about such a traumatic event. This must be incredibly difficult for you to talk about. If you're comfortable, please share your feelings or thoughts, and I'll listen.",
        "I can't imagine how challenging this must be for you. If you want to talk about it, I'm here to provide support and a listening ear.",
    ])
    return response

  if 'privacy' in words or 'talk about it' in words:
    response = random.choice([
        "I respect your boundaries, and you're in control of how much you want to share. Please know that you can talk to me about anything you're comfortable with.",
        "You have the right to decide how much you want to discuss this. Whenever you're ready, I'm here to listen.",
    ])
    return response

  if 'feel alone' in words or 'need someone' in words:
    response = random.choice([
        "You're not alone. I'm here to support you. How can I help?",
        "I'm here to talk and listen. What's been on your mind?",
    ])
    return response

  if 'self-care' in words or 'take care of myself' in words:
    response = random.choice([
        "Self-care is important. What are some things you enjoy doing to take care of yourself?",
        "Remember to prioritize self-care. It's essential for your well-being.",
    ])
    return response

  if 'anxious' in words or 'nervous' in words:
    response = random.choice([
        "It's common to feel anxious at times. Let's explore what's causing your anxiety.",
        "I'm here to help you manage your anxiety. What's been making you feel this way?",
    ])
    return response

  if 'cope' in words or 'deal with' in words:
    response = random.choice([
        "Coping with difficult situations can be challenging. What strategies have you tried?",
        "Let's talk about coping strategies. What works best for you when you're facing difficulties?",
    ])
    return response

  if 'mindfulness' in words or 'meditate' in words:
    response = random.choice([
        "Mindfulness can be a great way to reduce stress. Have you tried meditation or deep breathing exercises?",
        "Mindfulness practices can help you stay present in the moment. Would you like some guidance on this?",
    ])
    return response

  if 'suicidal' in words or 'want to die' in words:
    response = random.choice([
        "I'm really sorry to hear that you're feeling this way. It's crucial to talk to someone who can help. Would you like to share more about what's going on?",
        "I'm here for you, but I can't provide the help that you need. It's essential to talk to a mental health professional or someone you trust about your feelings.",
    ])
    return response

  if 'help with suicide' in words or 'suicide prevention' in words:
    response = random.choice([
        "I'm not equipped to provide the assistance you need, but there are people who can help. Please consider reaching out to a mental health hotline or a trusted friend or family member.",
        "Your well-being is important. You can contact a suicide prevention hotline or a mental health professional for support.",
    ])
    return response

  if 'talk to someone' in words or 'need to talk' in words:
    response = random.choice([
        "Talking about your feelings can make a significant difference. Consider reaching out to someone you trust or a mental health professional.",
        "You don't have to face this alone. Please talk to someone who can provide the help and support you need.",
    ])
    return response
  
  if 'conflict resolution' in words or 'anger management' in words:
    response = random.choice([
        "It's important to find non-violent ways to address conflicts and manage anger. Have you considered seeking help or resources for conflict resolution?",
        "Conflict resolution and anger management skills can be beneficial. Let's explore options for addressing issues in a healthy way.",
    ])
    return response

  if 'crisis helpline' in words or 'emergency help' in words:
    response = random.choice([
        "If you're in immediate distress, please reach out to a crisis helpline or call emergency services. Your safety and the safety of others is crucial.",
        "Your well-being is important. You can contact a crisis helpline to speak with professionals who can assist you during this challenging time.",
    ])
    return response

  if 'want to kill' in words or 'hurt someone' in words:
    response = random.choice([
        "I'm really sorry to hear that you're feeling this way, but I can't provide the help you need. It's crucial to talk to a mental health professional or a trusted person about your feelings. Please seek help immediately.",
        "It's important to prioritize safety. If you're in crisis or experiencing harmful thoughts, please contact a mental health crisis hotline or a trusted person who can assist you.",
    ])
    return response


  if 'safety' in words or 'stay safe' in words:
    response = random.choice([
        "Your safety is our top priority. If you're in immediate danger, please call emergency services or a crisis helpline in your area.",
        "Staying safe is crucial. If you're in crisis, please seek help right away.",
    ])
    return response

  if 'abuse' in words or 'abusive' in words:
    response = random.choice([
        "I'm so sorry to hear that you've experienced abuse. It's crucial to talk to someone who can help and provide support. Would you like to share more about what's happened?",
        "I'm here to listen and support you, but it's essential to reach out to a professional who can provide the help you need. Please consider talking to a mental health expert or a trusted person about your experiences.",
    ])
    return response
  

  if 'help for abuse' in words or 'abuse support' in words:
    response = random.choice([
        "There are resources available to help individuals who have experienced abuse. You might want to reach out to a support organization or a counselor who specializes in trauma and abuse recovery.",
        "Support is available for survivors of abuse. You can contact a local abuse hotline or seek guidance from a therapist who can help you navigate the healing process.",
    ])
    return response

  
  if emotion:
        if emotion in positive_emotions:
            response = random.choice([
                "That's great! What's making you feel " + emotion + "?",
                "I'm glad to hear that you're feeling " + emotion + ". Tell me more about it.",
            ])
        elif emotion in negative_emotions:
            response = random.choice([
                "I'm sorry to hear that you're feeling " + emotion + ". Can you tell me more about it?",
                "It's normal to feel " + emotion + " sometimes. What's been bothering you?",
            ])
        return response
  
  if any(greeting in words for greeting in ['hello', 'hi', 'hey', 'greetings', 'howdy']):
    response = random.choice([
        "Hello! How can I help you today?",
        "Hi there! What's on your mind?",
        "Hey! What can I assist you with?",
        "Greetings! How can I be of service?",
        "Howdy! What's going on in your world?",
    ])
    return response 
  
  if 'pet' in words:
      response = random.choice([
          "Pets can be wonderful companions. Tell me more about your pet. What kind of pet do you have?",
          "Pets bring so much joy. What's your pet's name, and what do you love most about them?",
      ])
      return response

  if 'dog' in words:
      response = random.choice([
          "Dogs are known for their loyalty and unconditional love. Do you have a dog? What's their name?",
          "Having a dog can be so rewarding. What's your favorite activity to do with your dog?",
          "Dogs are great listeners. They make wonderful companions. How long have you had your dog?",
      ])
      return response

  if 'cat' in words:
    response = random.choice([
        "Cats are independent and mysterious. Do you have a cat as a pet? What's their personality like?",
        "Cats can be so charming and graceful. What's your favorite memory with your cat?",
        "Cats are known for their purring. How does your cat show affection?",
    ])
    return response

  if 'bird' in words:
    response = random.choice([
        "Birds are fascinating creatures with beautiful plumage. What kind of bird do you have as a pet?",
        "Birds can be quite talkative. Does your pet bird mimic sounds or talk?",
        "Birds have unique personalities. What's the most interesting thing your pet bird does?",
    ])
    return response

  if 'fish' in words:
      response = random.choice([
        "Fish can be very calming to watch. Do you have an aquarium with pet fish?",
        "Maintaining an aquarium can be a relaxing hobby. What types of fish do you have?",
        "Fish come in a variety of colors and sizes. What's your favorite fish in your aquarium?",
      ])
      return response


  if 'how are you' in words: 
      response = random.choice([
          "I'm just a computer program, so I don't have feelings, but I'm here to help you.",
          "I'm here to listen. What's on your mind?",
      ])
      return response 

  if 'hurt' in words or 'hurts' in words:
        response = random.choice([
            "I'm here to listen. Can you tell me more about the pain you're experiencing?",
            "I'm here to support you. Can you describe the pain in more detail?",
            "Pain can be tough. I'm here to talk about it. Tell me more.",
        ])
        return response
  
  if 'i need' in line:
        response = random.choice([
            "What do you think you need that for? Tell me more about it.",
            "Why do you feel you need that? Let's talk about it.",
            "I'm here to help. Can you explain why you need that?",
        ])
        return response
  
  if 'died' in line or 'passed away' in line:
        response = random.choice([
          "I'm truly sorry to hear about your loss. Losing someone can be incredibly tough. If you'd like to talk about it or share your feelings, I'm here to listen.",
          "Losing someone you care about is never easy. My condolences. If you want to share your memories or thoughts, I'm here for you.",
        ])
        return response

  

  if 'goodbye' in words or 'bye' in words or 'good bye' in words:
        response = random.choice([
            "Goodbye! Take care.",
            "It was nice talking to you. Goodbye!",
            "Farewell! Feel free to come back anytime.",
        ])
        return response
  
  response = random.choice([
    "Can you tell me more about that?",
    "I'd love to hear your thoughts on this.",
    "What led you to this conclusion?",
    "Interesting, can you elaborate further?",
    "Tell me, how did you come to that conclusion?",
    "I'm here to listen. Please feel free to share your thoughts and feelings.",
    "Thank you for sharing. I'm here to support you in any way I can.",
    "It's important to express your emotions. How are you feeling right now?",
  ])
  return response


# Main chat loop

print('Renee: Hello. My name is Renee, i\'m a working theropy bot. What\'s your name?')
name = input('You: ')
print ('Renee: It\'s nice to meet you, ', name, '!')
print ('Renee: Type \"exit\" whenever you want to exit this chat program.')
print ("Renee: Well, "+name+", what's on your mind? ")
line = input (name + ': ')
while line!="exit":
  line = line.lower()
  #print (line) #testing line delete
  reply = getReply(line, line.split())
  print ('Renee: '+reply)
  line = input(name + ': ')
