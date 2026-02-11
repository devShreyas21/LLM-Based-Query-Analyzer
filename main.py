from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# defining a pydantic for structured output parser
class QueryAnalysis(BaseModel):

    intent: str = Field(description="Primary intent of the user query")
    topic: str = Field(description="Main topic of the query")
    urgency: str = Field(description="low, medium or high")
    summary: str = Field(description="One sentence summary")

# passing the pydantantic into parser
parser = PydanticOutputParser(pydantic_object=QueryAnalysis)

# creating a prompt template
prompt = PromptTemplate(
    template='''

You are a AI system that analyzes user queries.

{format_instructions}

User query :
{query}

''',

input_variables=['query'],

partial_variables={
    "format_instructions":parser.get_format_instructions()
}
)

# creating model 
llm = ChatOpenAI()

# creating chain
chain = prompt | llm | parser

if __name__ == "__main__":
    user_query = input("Enter your query : ")
    result = chain.invoke({"query":user_query})
    print("\n Structured output \n ",result)
