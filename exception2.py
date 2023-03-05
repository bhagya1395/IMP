{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16033e52",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "try:\n",
    "    print(\"try\")\n",
    "    os._exit(0)\n",
    "except ZeroDivisionError:\n",
    "    print(\"Except\")\n",
    "finally:\n",
    "    print(\"finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e3b80cb5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "2.0\n",
      "iam here\n",
      "from nanded\n",
      "this is normal temination of program\n"
     ]
    }
   ],
   "source": [
    "#control-flow in try-except-finally block:\n",
    "#case-1:if there is no excetion\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(10/5)\n",
    "    print(\"iam here\")\n",
    "except exception:\n",
    "    print(\"kanchan\")\n",
    "finally:\n",
    "    print(\"from nanded\")\n",
    "print(\"this is normal temination of program\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f7ae1325",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "problem is: division by zero\n",
      "from nanded\n",
      "this is normal temination of program\n"
     ]
    }
   ],
   "source": [
    "#case-2:if an exception raised at stmt-2 and mached except block is available\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(10/0)\n",
    "    print(\"iam here\")\n",
    "except Exception as msg:\n",
    "    print(\"problem is:\",msg)\n",
    "finally:\n",
    "    print(\"from nanded\")\n",
    "print(\"this is normal temination of program\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f13c2421",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "from nanded\n"
     ]
    },
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [6]\u001b[0m, in \u001b[0;36m<cell line: 4>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m      5\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhello\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 6\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;241;43m10\u001b[39;49m\u001b[38;5;241;43m/\u001b[39;49m\u001b[38;5;241;43m0\u001b[39;49m)\n\u001b[0;32m      7\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124miam here\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      8\u001b[0m \u001b[38;5;66;03m#except:\u001b[39;00m\n\u001b[0;32m      9\u001b[0m \u001b[38;5;66;03m#    print(\"hii\")\u001b[39;00m\n\u001b[0;32m     10\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "#case-3:if an exception raised at stmt-2 and mached except block is not\n",
    "#available\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(10/0)\n",
    "    print(\"iam here\")\n",
    "#except:\n",
    "#    print(\"hii\")\n",
    "finally:\n",
    "    print(\"from nanded\")\n",
    "print(\"this is abnormal temination of program\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "db445bae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "hii\n",
      "iam here\n",
      "from nanded\n",
      "this is abnormal temination of program\n"
     ]
    }
   ],
   "source": [
    "#case-4:if an exception raised at stmt-4 and it is always  abnormal trmination,\n",
    "#but before abnormal termination at stmt-5 will be executed\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(\"hii\")\n",
    "    print(\"iam here\")\n",
    "except Exceptoin as msg:\n",
    "    print(10/0,msg)\n",
    "finally:\n",
    "    print(\"from nanded\")\n",
    "print(\"this is abnormal temination of program\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "50bd4574",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "2.0\n",
      "iam here\n"
     ]
    },
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [4]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      8\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mproblem is:\u001b[39m\u001b[38;5;124m\"\u001b[39m,msg)\n\u001b[0;32m      9\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[1;32m---> 10\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;241;43m10\u001b[39;49m\u001b[38;5;241;43m/\u001b[39;49m\u001b[38;5;241;43m0\u001b[39;49m)\n\u001b[0;32m     11\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mthis is abnormal temination of program\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "#case-5:if an exception raised at stmt-5 and it is always abnormal termination\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(10/5)\n",
    "    print(\"iam here\")\n",
    "except Exception as msg:\n",
    "    print(\"problem is:\",msg)\n",
    "finally:\n",
    "    print(10/0)\n",
    "print(\"this is abnormal temination of program\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b0f269ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "2.0\n",
      "iam here\n",
      "finally\n"
     ]
    },
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [5]\u001b[0m, in \u001b[0;36m<cell line: 10>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[0;32m      9\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfinally\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m---> 10\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;241;43m10\u001b[39;49m\u001b[38;5;241;43m/\u001b[39;49m\u001b[38;5;241;43m0\u001b[39;49m)\n",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "#case-6:if an exception raised at stmt-6 and it is always abnormal termination\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(10/5)\n",
    "    print(\"iam here\")\n",
    "except Exception as msg:\n",
    "    print(\"problem is:\",msg)\n",
    "finally:\n",
    "    print(\"finally\")\n",
    "print(10/0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a84c4ead",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "outer try block\n",
      "inner try block\n",
      "inner except block\n",
      "inner finally block\n",
      "outer finally block\n"
     ]
    }
   ],
   "source": [
    "#Neasted try-except-finally block\n",
    "\n",
    "try:\n",
    "    print(\"outer try block\")\n",
    "    \n",
    "    try:\n",
    "        print(\"inner try block\")\n",
    "        print(10/0)\n",
    "    except Exception:\n",
    "        print(\"inner except block\")\n",
    "    finally:\n",
    "        print(\"inner finally block\")\n",
    "except:\n",
    "    print(\"outer except block\")\n",
    "finally:\n",
    "    print(\"outer finally block\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "24ed6381",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "iam kanchan\n",
      "from nanded\n",
      "hii\n",
      "this is teambrainworks\n",
      "python\n",
      "iam inner finally block\n",
      "this is  inner normal flow of program\n",
      "iam outer finally block\n",
      "this is outer normal flow of program \n"
     ]
    }
   ],
   "source": [
    "#case-1:if there is no exception\n",
    "    \n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(\"iam kanchan\")\n",
    "    print(\"from nanded\")\n",
    "    try:\n",
    "        print(\"hii\")\n",
    "        print(\"this is teambrainworks\")\n",
    "        print(\"python\")\n",
    "    except exception as msg1:\n",
    "        print(\"this is problem:\",msg1)\n",
    "    finally:\n",
    "        print(\"iam inner finally block\")\n",
    "    print(\"this is  inner normal flow of program\")\n",
    "except exception as msg2:\n",
    "    print(\"this is problem:\",msg2)\n",
    "finally:\n",
    "    print(\"iam outer finally block\")\n",
    "print(\"this is outer normal flow of program \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "44e3c9a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "it is outer exception block: division by zero\n",
      "iam outer finally block\n",
      "this is outer normal flow of program \n"
     ]
    }
   ],
   "source": [
    "#case-2:if there exception raised at stmt-2 and corresponding except block match\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(10/0)\n",
    "    print(\"from nanded\")\n",
    "    try:\n",
    "        print(\"hii\")\n",
    "        print(\"this is teambrainworks\")\n",
    "        print(\"python\")\n",
    "    except Exception as msg1:\n",
    "        print(\"it is inner exception block:\",msg1)\n",
    "    finally:\n",
    "        print(\"iam inner finally block\")\n",
    "    print(\"this is  inner normal flow of program\")\n",
    "except Exception as msg2:\n",
    "    print(\"it is outer exception block:\",msg2)\n",
    "finally:\n",
    "    print(\"iam outer finally block\")\n",
    "print(\"this is outer normal flow of program \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "eeb3098e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "iam outer finally block\n"
     ]
    },
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [22]\u001b[0m, in \u001b[0;36m<cell line: 4>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m      5\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhello\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 6\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;241;43m10\u001b[39;49m\u001b[38;5;241;43m/\u001b[39;49m\u001b[38;5;241;43m0\u001b[39;49m)\n\u001b[0;32m      7\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfrom nanded\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      8\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "#case-3:if there is exception raised at stmt-2 and corresponding except\n",
    "# block not match\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(10/0)\n",
    "    print(\"from nanded\")\n",
    "    try:\n",
    "        print(\"hii\")\n",
    "        print(\"this is teambrainworks\")\n",
    "        print(\"python\")\n",
    "    except Exception as msg1:\n",
    "        print(\"it is inner exception block:\",msg1)\n",
    "    finally:\n",
    "        print(\"iam inner finally block\")\n",
    "    print(\"this is  inner normal flow of program\")\n",
    "except ValueError as msg:\n",
    "    print(\"it is outer exception block:\",msg)\n",
    "finally:\n",
    "    print(\"iam outer finally block\")\n",
    "print(\"this is outer normal flow of program \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8883843a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "iam kanchan\n",
      "from nanded\n",
      "hii\n",
      "it is inner exception block: division by zero\n",
      "iam inner finally block\n",
      "this is  inner normal flow of program\n",
      "iam outer finally block\n",
      "this is outer normal flow of program \n"
     ]
    }
   ],
   "source": [
    "#case-4:if there is exception raised at stmt-5 and corresponding inner except\n",
    "# block matched\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(\"iam kanchan\")\n",
    "    print(\"from nanded\")\n",
    "    try:\n",
    "        print(\"hii\")\n",
    "        print(10/0)\n",
    "        print(\"python\")\n",
    "    except Exception as msg1:\n",
    "        print(\"it is inner exception block:\",msg1)\n",
    "    finally:\n",
    "        print(\"iam inner finally block\")\n",
    "    print(\"this is  inner normal flow of program\")\n",
    "except ValueError as msg:\n",
    "    print(\"it is outer exception block:\",msg)\n",
    "finally:\n",
    "    print(\"iam outer finally block\")\n",
    "print(\"this is outer normal flow of program \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "58dd5500",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "iam kanchan\n",
      "from nanded\n",
      "hii\n",
      "it is inner exception block:\n",
      "iam inner finally block\n",
      "this is  inner normal flow of program\n",
      "iam outer finally block\n",
      "this is outer normal flow of program \n"
     ]
    }
   ],
   "source": [
    "#case-5:if there is exception raised at stmt-5 and corresponding inner except\n",
    "# block not matched but outer except block matched\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(\"iam kanchan\")\n",
    "    print(\"from nanded\")\n",
    "    try:\n",
    "        print(\"hii\")\n",
    "        print(10/0)\n",
    "        print(\"python\")\n",
    "    except:\n",
    "        print(\"it is inner exception block:\")\n",
    "    finally:\n",
    "        print(\"iam inner finally block\")\n",
    "    print(\"this is  inner normal flow of program\")\n",
    "except ZeroDivisionError as msg2:\n",
    "    print(\"it is outer exception block:\",msg2)\n",
    "finally:\n",
    "    print(\"iam outer finally block\")\n",
    "print(\"this is outer normal flow of program \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c1f8960f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "iam kanchan\n",
      "from nanded\n",
      "hii\n",
      "iam inner finally block\n",
      "iam outer finally block\n"
     ]
    },
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [27]\u001b[0m, in \u001b[0;36m<cell line: 4>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m      9\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhii\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m---> 10\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;241;43m10\u001b[39;49m\u001b[38;5;241;43m/\u001b[39;49m\u001b[38;5;241;43m0\u001b[39;49m)\n\u001b[0;32m     11\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     12\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m msg1:\n",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "#case-6:if there is exception raised at stmt-5 and  both corresponding inner \n",
    "#  except block and  outer except block  not matched\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(\"iam kanchan\")\n",
    "    print(\"from nanded\")\n",
    "    try:\n",
    "        print(\"hii\")\n",
    "        print(10/0)\n",
    "        print(\"python\")\n",
    "    except KeyError as msg1:\n",
    "        print(\"it is inner exception block:\",msg1)\n",
    "    finally:\n",
    "        print(\"iam inner finally block\")\n",
    "    print(\"this is  inner normal flow of program\")\n",
    "except ValueError as msg2:\n",
    "    print(\"it is outer exception block:\",msg2)\n",
    "finally:\n",
    "    print(\"iam outer finally block\")\n",
    "print(\"this is outer normal flow of program \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8e05db9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "iam kanchan\n",
      "from nanded\n",
      "hii\n",
      "this is tambrainworks\n",
      "python\n",
      "iam inner finally block\n",
      "this is  inner normal flow of program\n",
      "iam outer finally block\n",
      "this is outer normal flow of program \n"
     ]
    }
   ],
   "source": [
    "#case-7:if there is exception raised at stmt-7 and corresponding except\n",
    "# block matched\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(\"iam kanchan\")\n",
    "    print(\"from nanded\")\n",
    "    try:\n",
    "        print(\"hii\")\n",
    "        print(\"this is tambrainworks\")\n",
    "        print(\"python\")\n",
    "    except ValueError:\n",
    "        print(10/0)\n",
    "    finally:\n",
    "        print(\"iam inner finally block\")\n",
    "    print(\"this is  inner normal flow of program\")\n",
    "except ZeroDivisionError as msg2:\n",
    "    print(\"it is outer exception block:\",msg2)\n",
    "finally:\n",
    "    print(\"iam outer finally block\")\n",
    "print(\"this is outer normal flow of program \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3e0f6dd7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "iam kanchan\n",
      "from nanded\n",
      "hii\n",
      "this is tambrainworks\n",
      "python\n",
      "iam inner finally block\n",
      "this is  inner normal flow of program\n",
      "iam outer finally block\n",
      "this is outer normal flow of program \n"
     ]
    }
   ],
   "source": [
    "#case-8:if exception raised at stmt-7 and corresponding except block not matched\n",
    "\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(\"iam kanchan\")\n",
    "    print(\"from nanded\")\n",
    "    try:\n",
    "        print(\"hii\")\n",
    "        print(\"this is tambrainworks\")\n",
    "        print(\"python\")\n",
    "    except ValueError:\n",
    "        print(10/0)\n",
    "    finally:\n",
    "        print(\"iam inner finally block\")\n",
    "    print(\"this is  inner normal flow of program\")\n",
    "except:\n",
    "    print(\"it is outer exception block:\")\n",
    "finally:\n",
    "    print(\"iam outer finally block\")\n",
    "print(\"this is outer normal flow of program \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ffa4faeb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "iam kanchan\n",
      "from nanded\n",
      "hii\n",
      "this is tambrainworks\n",
      "python\n",
      "it is outer exception block: division by zero\n",
      "iam outer finally block\n",
      "this is outer normal flow of program \n"
     ]
    }
   ],
   "source": [
    "#case-9:if exception raised at stmt-8 and corresponding except block  matched\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(\"iam kanchan\")\n",
    "    print(\"from nanded\")\n",
    "    try:\n",
    "        print(\"hii\")\n",
    "        print(\"this is tambrainworks\")\n",
    "        print(\"python\")\n",
    "    except ValueError:\n",
    "        print(\"inner except block\")\n",
    "    finally:\n",
    "        print(10/0)\n",
    "    print(\"this is  inner normal flow of program\")\n",
    "except ZeroDivisionError as msg2:\n",
    "    print(\"it is outer exception block:\",msg2)\n",
    "finally:\n",
    "    print(\"iam outer finally block\")\n",
    "print(\"this is outer normal flow of program \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "64f14dc6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "iam kanchan\n",
      "from nanded\n",
      "hii\n",
      "this is tambrainworks\n",
      "python\n",
      "iam inner finally block\n",
      "it is outer exception block: division by zero\n",
      "iam outer finally block\n",
      "this is outer normal flow of program \n"
     ]
    }
   ],
   "source": [
    "#case-10:if exception raised at stmt-9 and corresponding except block  matched\n",
    "\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(\"iam kanchan\")\n",
    "    print(\"from nanded\")\n",
    "    try:\n",
    "        print(\"hii\")\n",
    "        print(\"this is tambrainworks\")\n",
    "        print(\"python\")\n",
    "    except ValueError:\n",
    "        print(\"inner except block\")\n",
    "    finally:\n",
    "        print(\"iam inner finally block\")\n",
    "    print(10/0)\n",
    "except ZeroDivisionError as msg2:\n",
    "    print(\"it is outer exception block:\",msg2)\n",
    "finally:\n",
    "    print(\"iam outer finally block\")\n",
    "print(\"this is outer normal flow of program \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "25869f0c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "iam kanchan\n",
      "from nanded\n",
      "hii\n",
      "this is tambrainworks\n",
      "python\n",
      "iam inner finally block\n",
      "iam outer finally block\n"
     ]
    },
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [9]\u001b[0m, in \u001b[0;36m<cell line: 4>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     15\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124miam inner finally block\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m---> 16\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;241;43m10\u001b[39;49m\u001b[38;5;241;43m/\u001b[39;49m\u001b[38;5;241;43m0\u001b[39;49m)\n\u001b[0;32m     17\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mZeroDivisionError\u001b[39;00m:\n",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [9]\u001b[0m, in \u001b[0;36m<cell line: 4>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     16\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;241m10\u001b[39m\u001b[38;5;241m/\u001b[39m\u001b[38;5;241m0\u001b[39m)\n\u001b[0;32m     17\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mZeroDivisionError\u001b[39;00m:\n\u001b[1;32m---> 18\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;241;43m10\u001b[39;49m\u001b[38;5;241;43m/\u001b[39;49m\u001b[38;5;241;43m0\u001b[39;49m)\n\u001b[0;32m     19\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[0;32m     20\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124miam outer finally block\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "#case-11:if exception raised at stmt-10 and corresponding except block  matched\n",
    "\n",
    "\n",
    "try:\n",
    "    print(\"hello\")\n",
    "    print(\"iam kanchan\")\n",
    "    print(\"from nanded\")\n",
    "    try:\n",
    "        print(\"hii\")\n",
    "        print(\"this is tambrainworks\")\n",
    "        print(\"python\")\n",
    "    except ValueError:\n",
    "        print(\"inner except block\")\n",
    "    finally:\n",
    "        print(\"iam inner finally block\")\n",
    "    print(10/0)\n",
    "except ZeroDivisionError:\n",
    "    print(10/0)\n",
    "finally:\n",
    "    print(\"iam outer finally block\")\n",
    "print(\"this is outer normal flow of program \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28e3a156",
   "metadata": {},
   "outputs": [],
   "source": [
    "#else block:else block wiil be executed if there is no excepton inside try block\n",
    "try:\n",
    "    Risky code\n",
    "except:\n",
    "    will be executed if an exception raised in try\n",
    "else:\n",
    "    will be executed if no exception  in try\n",
    "finally:\n",
    "    will be executed always whether exception raised or not raised\n",
    "    and handle or not handle\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e934a5e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try\n",
      "else\n",
      "fially\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    print(\"try\")\n",
    "    #print(10/0)\n",
    "except:\n",
    "    print(\"except\")\n",
    "else:\n",
    "    print(\"else\")\n",
    "finally:\n",
    "    print(\"fially\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "1e15158d",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "incomplete input (3543163043.py, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [18]\u001b[1;36m\u001b[0m\n\u001b[1;33m    \u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m incomplete input\n"
     ]
    }
   ],
   "source": [
    "#varieous possible combinations of try-except-else-finally block:\n",
    "#1)try block compulsory we should write either except or finally block\n",
    "#2) except without try is invalid\n",
    "#3)finally without try is invalid\n",
    "#4)we can take multiple except block for the same try but can't take\n",
    "#multipe else and finally block\n",
    "#5)else without except is invalid\n",
    "#6)try-except-else-finally order is important\n",
    "#7)we can take try-except-else-finally in try ,except,else,finally blocks.\n",
    "#neasting of try-except-else-finally is possible\n",
    "#1)\n",
    "try:\n",
    "    print(\"hello\")#without except and finally block it is invalid\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e43f36f4",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (657883304.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [19]\u001b[1;36m\u001b[0m\n\u001b[1;33m    except:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#2)\n",
    "except:\n",
    "    print(\"except\")#without try only except block is always invalid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "e38ad035",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2564211622.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [20]\u001b[1;36m\u001b[0m\n\u001b[1;33m    else:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#3)\n",
    "else:\n",
    "    print(\"else\")#it is invalid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "2c0cb4c8",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (555858639.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [22]\u001b[1;36m\u001b[0m\n\u001b[1;33m    finally:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#4)\n",
    "finally:\n",
    "    print(\"finally\")#it is invalid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "be590d68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try\n"
     ]
    }
   ],
   "source": [
    "#5)it is valid\n",
    "try:\n",
    "    print(\"try\")\n",
    "except:\n",
    "    print(\"except\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "8211a6d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try\n",
      "finally\n"
     ]
    }
   ],
   "source": [
    "#6)it is valid\n",
    "try:\n",
    "    print(\"try\")\n",
    "   # print(10/0)\n",
    "finally:\n",
    "    print(\"finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e39b701e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try\n",
      "except\n"
     ]
    }
   ],
   "source": [
    "#7)it is valid\n",
    "try:\n",
    "    print(\"try\")\n",
    "    #print(10/0)\n",
    "except:\n",
    "    print(\"except\")\n",
    "else:\n",
    "    print(\"else\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "c0173fb0",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "expected 'except' or 'finally' block (1895272735.py, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [31]\u001b[1;36m\u001b[0m\n\u001b[1;33m    else:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m expected 'except' or 'finally' block\n"
     ]
    }
   ],
   "source": [
    "#8)it is invalid,whenever we write else block is coumplsory except \n",
    "#block required\n",
    "try:\n",
    "    print(\"try\")\n",
    "else:\n",
    "    print(\"else\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "41803827",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "expected 'except' or 'finally' block (2460312907.py, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [33]\u001b[1;36m\u001b[0m\n\u001b[1;33m    else:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m expected 'except' or 'finally' block\n"
     ]
    }
   ],
   "source": [
    "#9)it is invlid\n",
    "\n",
    "try:\n",
    "    print(\"try\")\n",
    "else:\n",
    "    print(\"else\") \n",
    "finally:\n",
    "    print(\"finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "f772d889",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try\n",
      "except-2\n"
     ]
    }
   ],
   "source": [
    "#10)it is valid\n",
    "try:\n",
    "    print(\"try\")\n",
    "    print(10/0)\n",
    "except ValueError:\n",
    "    print(\"except-1\")\n",
    "except ZeroDivisionError: \n",
    "    print(\"except-2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "6041875d",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3642809678.py, line 9)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [39]\u001b[1;36m\u001b[0m\n\u001b[1;33m    else:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#11)it is invalid\n",
    "try:\n",
    "    print(\"try\")\n",
    "    \n",
    "except ValueError:\n",
    "    print(\"except\")\n",
    "else:\n",
    "    print(\"else-1\")\n",
    "else:\n",
    "    print(\"else-2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "0a48e4b4",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (53470531.py, line 9)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [40]\u001b[1;36m\u001b[0m\n\u001b[1;33m    finally:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#12)it is invalid\n",
    "try:\n",
    "    print(\"try\")\n",
    "    print(10/0)\n",
    "except ZeroDivisionError: \n",
    "    print(\"except\")\n",
    "finally:\n",
    "    print(\"finally-1\")\n",
    "finally:\n",
    "    print(\"finally-2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "33fe455a",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "expected 'except' or 'finally' block (454232616.py, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [41]\u001b[1;36m\u001b[0m\n\u001b[1;33m    print(\"hello\")\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m expected 'except' or 'finally' block\n"
     ]
    }
   ],
   "source": [
    "#13) it is invalid\n",
    "try:\n",
    "    print(\"try\")\n",
    "print(\"hello\")\n",
    "except:\n",
    "    print(\"except\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "e2ff4d15",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1018582969.py, line 8)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [42]\u001b[1;36m\u001b[0m\n\u001b[1;33m    except ZeroDivisionError:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#14)it is invalid\n",
    "try:\n",
    "    print(\"try\")\n",
    "    print(10/0)\n",
    "except:\n",
    "    print(\"except\")\n",
    "print(\"hello\")\n",
    "except ZeroDivisionError: \n",
    "    print(\"except\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "8f13d4cf",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (227121269.py, line 7)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [43]\u001b[1;36m\u001b[0m\n\u001b[1;33m    finally:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#15) it is invalid\n",
    "try:\n",
    "    print(\"try\")\n",
    "except :\n",
    "    print(\"except\")\n",
    "print(\"hello\")\n",
    "finally:\n",
    "    print(\"finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "09ba1443",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1002489782.py, line 7)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [44]\u001b[1;36m\u001b[0m\n\u001b[1;33m    else:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#16) it is invalid\n",
    "try:\n",
    "    print(\"try\")\n",
    "except :\n",
    "    print(\"except\")\n",
    "print(\"hello\")\n",
    "else:\n",
    "    print(\"else\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "25729cd2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try-1\n",
      "try-2\n",
      "finally\n"
     ]
    }
   ],
   "source": [
    "#17) it is valid\n",
    "try:\n",
    "    print(\"try-1\")\n",
    "except :\n",
    "    print(\"except\")\n",
    "try:\n",
    "    print(\"try-2\")\n",
    "finally:\n",
    "    print(\"finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "9056deb3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try-1\n",
      "try-2\n"
     ]
    }
   ],
   "source": [
    "#18) it is valid\n",
    "try:\n",
    "    print(\"try-1\")\n",
    "except :\n",
    "    print(\"except\")\n",
    "try:\n",
    "    print(\"try-2\")\n",
    "except:\n",
    "    print(\"except\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "1ba8a55c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try\n",
      "else\n"
     ]
    }
   ],
   "source": [
    "#19) it is valid\n",
    "try:\n",
    "    print(\"try\")\n",
    "except :\n",
    "    print(\"except\")\n",
    "if 10>20:\n",
    "    print(\"if\")\n",
    "else:\n",
    "    print(\"else\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "177caec5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try\n",
      "inner try\n",
      "inner finally\n",
      "finally\n"
     ]
    }
   ],
   "source": [
    "#20) it is valid\n",
    "try:\n",
    "    print(\"try\")\n",
    "    try:\n",
    "        print(\"inner try\")\n",
    "    except:\n",
    "        print(\"inner except\")\n",
    "    finally:\n",
    "        print(\"inner finally\")\n",
    "except :\n",
    "    print(\"except\")\n",
    "finally:\n",
    "    print(\"finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "6d1fb708",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try\n"
     ]
    }
   ],
   "source": [
    "#20) it is valid\n",
    "try:\n",
    "    print(\"try\")\n",
    "except :\n",
    "    try:\n",
    "        print(\"inner try\")\n",
    "    except:\n",
    "        print(\"inner except\")\n",
    "    finally:\n",
    "        print(\"inner finally\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "761244f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "try\n",
      "Inner try\n",
      "Inner finally\n"
     ]
    }
   ],
   "source": [
    "#21)  it is valid\n",
    "try:\n",
    "    print(\"try\")\n",
    "except :\n",
    "    print(\"except\")\n",
    "finally:\n",
    "    try:\n",
    "        print(\"Inner try\")\n",
    "    except:\n",
    "        ptint(\"except\")\n",
    "    finally:\n",
    "        print(\"Inner finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "b7a51880",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "expected 'except' or 'finally' block (59847389.py, line 8)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [52]\u001b[1;36m\u001b[0m\n\u001b[1;33m    else:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m expected 'except' or 'finally' block\n"
     ]
    }
   ],
   "source": [
    "#22)  it is invalid\n",
    "try:\n",
    "    print(\"try-1\")\n",
    "except :\n",
    "    print(\"except\")\n",
    "try:\n",
    "    print(\"try-2\")\n",
    "else:\n",
    "    print(\"else\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "f02d2787",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "incomplete input (3918988018.py, line 9)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [56]\u001b[1;36m\u001b[0m\n\u001b[1;33m    print(\"finally\")\u001b[0m\n\u001b[1;37m                    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m incomplete input\n"
     ]
    }
   ],
   "source": [
    "#23)  it is invalid\n",
    "try:\n",
    "    print(\"try\")\n",
    "    try:\n",
    "        print(\"Inner try\")\n",
    "except:\n",
    "    print(\"except\")\n",
    "finally:\n",
    "    print(\"finally\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67ea6e0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#types of exception:\n",
    "#there are two types of exceptions:\n",
    "1)predefined exceptions/In built exceptions\n",
    "2)User defined exceptions/coustmized exception"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "ba79960e",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: 'ten'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Input \u001b[1;32mIn [59]\u001b[0m, in \u001b[0;36m<cell line: 6>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m#1)predefined exceptions/In built exceptions:\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;66;03m#>>the exceptions which are raised automaticlly by python whenever\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;66;03m#a perticular event occurs\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;66;03m#eg:\u001b[39;00m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;66;03m#print(10/0)#>>Zerodivision error\u001b[39;00m\n\u001b[1;32m----> 6\u001b[0m x\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;43mint\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mten\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: 'ten'"
     ]
    }
   ],
   "source": [
    "#1)predefined exceptions/In built exceptions:\n",
    "#>>the exceptions which are raised automaticlly by python whenever\n",
    "#a perticular event occurs\n",
    "#eg:\n",
    "print(10/0)#>>Zerodivision error\n",
    "x=int(\"ten\")#>>value error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "f4931f1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#2)User defined exceptions/coustmized exceptions:\n",
    "#exception raised by programmer\n",
    "#Q) how to define and raise customized exceptions:\n",
    "class ToOldException(Exception):\n",
    "    def __init__(self,arg):\n",
    "        self.msg=arg\n",
    "        \n",
    "        \n",
    "class ToYoungException(Exception):\n",
    "    def __init__(self,arg):\n",
    "        self.msg=arg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "79500b53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter age:25\n",
      "thanks for registrtion... you will get matched detail by mail\n"
     ]
    }
   ],
   "source": [
    "class ToOldException(Exception):\n",
    "    def __init__(self,arg):\n",
    "        self.msg=arg\n",
    "        \n",
    "        \n",
    "class ToYoungException(Exception):\n",
    "    def __init__(self,arg):\n",
    "        self.msg=arg    \n",
    "age=int(input(\"enter age:\"))\n",
    "if age>60:\n",
    "    raise ToYoungException(\"plez wait some more time definately you will get best matched\")\n",
    "elif age<18:\n",
    "    raise ToOldException(\"your age already crossed marriage age no chance to get marrige\")\n",
    "else:\n",
    "    print(\"thanks for registrtion... you will get matched detail by mail\")\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea414db8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
