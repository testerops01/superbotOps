from autogen.agentchat import Agent,AssistantAgent,UserProxyAgent
from typing import Dict,Optional,Union,Callable
import chainlit as cl

async def ask_helper(func, **kwargs):
    res = await func(**kwargs).send()
    while not res:
        res = await func(**kwargs).send()
    return res


class ChainlitAssistantAgent(AssistantAgent):
    """
    Wrapper for Autogen Assistant agents
    """

    def send(self,
             message: Union[Dict,str],
             recipient : Agent,
             request_reply: Optional[bool] = None,
             silent: Optional[bool] = False,
             ) -> bool:
        cl.run_sync(
            cl.Message(
                content=f'*Sending message to "{recipient.name}":*\n\n{message}',
                author=self.name,
            ).send()
        )

        super(ChainlitAssistantAgent, self).send(
            message= message,
            recipient=recipient,
            request_reply=request_reply,
            silent=silent
        )