import base64 as Base64
import requests as Requests
import json as JSON
import random as Random
import time as Time
from solver import Funcaptcha

Funcaptcha = Funcaptcha()

LOGIN_API = "https://auth.roblox.com/v2/login"
CONTINUE_API = "https://apis.roblox.com/challenge/v1/continue"
ROBLOX_URL = "https://www.roblox.com"
JS_URL = "https://roblox-api.arkoselabs.com"

ROBLOX_KEY = "476068BF-9607-4799-B53D-966BE98E2B81"
ROBLOX_BDA = "eyJjdCI6IlVlSlkxWk54Qm1ZR2ZaOUhIL2c1WkljdkY1TG04SS9jSnZURVRsU2xwVENXeGJCOW8wbVNFaVFJbThVdDdzSk9kZDNEd2N4Q1JMUVlCVk1jUmYyU05QUFljeWF3VDdWVXk2UUZiVXJlZ2NwcFpQNWxmWEFCVjR6RkpwdUFGQ09ObmNQa2g0eFJVQ1RXOEp6d3plQzRnSXp5RVV4QVVhaFFzRlFNanYrKzFTV3pQVUV1Vm1wc2RZVjIrRVNPeWRNcW5sWk1LMWF1cFhZR2NlRGx1dms2YWlpaTJ3RktwaHdzT0Zjd0oxVU9odUtBNWxOc3JPaW56ZnBiNGU2SGtjSXFpVllKL0UxTVB0R09wUEV4bDZ2enZ2MWk4amlzOXNncUlKZjZyNjV6clZZNmdHSmdFeFpOQjh4dWMzdUxRRXY2ZG4rOElPdmZKMFFFbXRtdTdWeXVIa3hDNm4rSnhxK1BWYVN5UGp6TEdDQ1Vla0p2QnpvZzBrSmVsb1R4SEF6RVlCS2FsbmE2TCtzMXFHczZaZ2ZueXBLZW94Wm1RVWJ3eTh1MVJDRFNOMmdXdlhqcDNWNGRhVmRPOXJ4cDBIeVN3UlA5QVZwTUdZZGYranM0R1J1NUNxTUVPbGZGNkVoT2Y1VmxqRWhpbFJ3QnIzVWVMdy9qcGM2c05NaWgvUjBHb2dEWUdDY1o3eW9DRklZQXZTVWQ5cTJnK0lNTXdNUmx1dXNpYms1aFhmZlBVY0JOU3U3V2tLbUlaMGl3RTRuOVd2RFJVa1I4WVBNZE5IcERhVy9PN0hpUTNReDZVTi9SVmdqbG94K2Vid2U3L3lvZzQzVk00VVRjUWFETUtiaEM4SkVJTGNZWGczd2l6MHIxaVpmdnRtYTBiVHNzTUVpd0h2cUk2eDJHOWxaQVV5WDRYRGNpcloxQ0orbm4zcW5HaEZKd2M3a0tpUE1uQzEwV3NqbTZIOUhEeUsraityQ2xkemlTY2VnU1k5WStsQkcyTDZhZXN2UGJvd0ZZU0lUSWFRTHRTOXMzMFE4cmhiaW5nUjVkS0hlVGpHbnV3ZXVjVThTa2hFalBmc292YWcreS9DalN1Y09IWGwvd2o2eC91MlFUSTA5VUZIbm42bWNVcFRKSDlrSEx4VXY4aWxDMVB1aStYRlg2M2hOdFpFdWljSjZ0T21YbVo4LzRDWkNoTmRTWXNUL1draXhJMjczaTBIakFOclMwdGRGeXRMYnZlYzlYdm9POW9CdGFiNk9jTWhzRVhSUW9EeEorb3RTODROb1cwd1lXQXN2VVp1RG5vSnJWZmxKcU9DYktMZ3FtRFk0T25HTFl3QUNBUTB1V0syVTRoZ3lRNEVGODhlUVRsU1ZOMXBsaENWQXhPMTZ2QjZCYWljZWJ1dFpRZFBwQ3Z1WmdJeFlLU0tOZE9zemRoVkxLaGd1QUttRVh3TXkycmk3ZEl6UlZPRVJpSm5ZOFp1ODJjQUZLT1hMay8weXdEYWZBZWVXWGtPVFM1akovMHJNUThFVFdpQm5ValBpYUE0eWdXN1ZVbFRUWnFZbUo0UHh3V1A0TWJDS0FJMjg1Q0cxVUJwVU4yVThOWm5NcjlIaXFTYW43TmIzTkFCZ21vZEl4QW5lWlljTE5xRlgwVzVCZnZqSmp5c1IyeTVhT29Zc3RweHBUZHhPamI4Y08ycDhOY3B2NS9XNGttalZuMzZWbzB2eXdkUkRLM1Fud2cvK2dYa1pZa0NsaGtBVERTNFE1RE9DQzVVUUZjdG80OFNadytaMlFGcDFTUHNMVGJESEZ5UjlJdTZ5dlNkNWs3bFEzRGlUdjJaQjlaNjZMMjNzUUxLdk9sclVWM3FtMEREcTV5MW9wQ0NiTjgvTzE2dFg5cVhKd0t1aSsrcXFZREwzWDgrVFpNaTJBRkFBQVhXcU9KQ1h4MzR3OCt3RXJKZVBhS3dPeU52TGRieFNhTTErQW05ODVIb0dsazFKUWZpRkJCMll0bkRsUmZqMXY2aDlsSno1bXVwT3ZvU3QxNnc4bTZGNE05aVBkb3ZhZDhJQjFLK3Fwd1JyVWM5djZaUTA1bUlJeXJMaVFCTjdSVW5OWnlzV2N2T21HanhyR0g4TmRXbGJjZ2pTYjc0RU95S0g3TVFkeXlDM2ZMRlFCekg0YytUZDlucEVjOFZxQjJYcW5zUUJDV0pCbCtwVzlDUjJHa20vMm5HS2UvZWsxMmNHUVQ3TVB4SHg1bXd5Y0duOEpzSUt3V3ZhaGE1djJ0K2ptZjVpem5ZdTZCSTdCNWhIYU01bTlENnROeHpqdEs1SjB5a0h2YldCQzdQeFlqWHoyWkZrK2JBbzAwVVJkWmZlOUVoekhmdnBzTE0vQnZNeEw5cmFxLzNPN1RNNG1pemI1NEdJWWliMWtVUk1iTzByQ1RLeGdqTUlycnpSMElrM3NrWlM1TGg3Vkd5Q1U4amxFQ1RzdzFwU1ZJOE1LSGVod1VJK21CeXo2UFlKa0RHZC9KNjZ3WWt1a0pDT3gyYVJDR084LzlseEpQdHpWRjdGeng3WnZIR1I5UDFWeURxUDUwdElpd0p1cS80aVlraTJmWUwwcm0yV0pyMHJPQXBPeHBlbkdKZ2dDaXVJZkg2Y2t1cldnWGtxV20rN09KTzVQVURnL3Q4WCtFRnVxVEJJVmhvcUpzZ0VQWEV4d0FSbyszd3RONzczdUVMMmRHWVNRb0ltU2UvRndlb3JzOVl3aFhpbXJuU2pZV2x0MFFpczBEMURjbmh4VFkwcndCQUxMakkvUTFaQ1lES0ZsUmFURE1FRHA0SDlDT1Z0S0QwYmRydlRUOHBFVDlLZE9KbW1MYSs4N2NkTVcwdW5IdFZ0K01YdXJBN21XOWQreUJEWHFlYnMvY0owUXM4c1Z5ejk2TkRIcHpsZ29YMzliRUk5YjV1WlZXRm96ZlZOc3NLOHl0TnN5NVBNM2ZINW5jL292bGQ5cTMyd3gyNmliVjhzYS9RQmZsOVB4VW9wdC8yM0pTT1pqeFlXbmdQTEg0NE1ZTUhyWWVqRHlCRTNhWXhOSCtONFo3Z2EvY2QxTHA1WU0yUE9aZW9ORjRydXJLa0JCWG5xVDJPTE5UaTQzRDhvYyt0c2VwVzBjWGtLd1NJRG1WQVNYcDBoRlhsYkpQNHZzYzdGQmVYeUNxSTZxVmVqWnlCN2hWSExPajdXN3NMZTR4cy9vR0xzMndLWWJ4aVk5TVNXcXJPeGF5dUhJUzFoYU1iWWhyTmxUOHJ2YWlKZnBvQ2NQUEJ4dG5kc0ZIcXV4WGw5OXI2Qis0ZEtINDFDa2ZFVEduNnNCaFhValdPcnBFYWJ0OWJSU2ZQSUxHWGs3NHlHVGV4Zm5PNlNPYmNRZk9BYnNBS3I5RENRZ1pUUEFBVHdicElZTW9vdTRranBVUVEvT2VTUEZKeXpESnBtODNBTlhzUkJVM2VsZWQzT2lhK1ByVnVWamV4UDBtK3V2QWYwMDlUU3hpOWZld0NXbVE5bWl2TWVqSlRaQW92Wkg1RlFOenZFMnFLVWcwS1dFUnF6WmVQM3ZBR2d2OFdoMHp2N0pkWVBwazFMRk1NOXF3ZGhaejdlRkY2N2t0Q0QySmovMlgrTmc1TStYcTNaRGtJMGN5azdMNGxqRW45VHVQcmcwbGFsbzFKSzJjdGVYNDZUaitjQ05uUW43QXR2M1ZHSWl2bzlGMENZTjhwSkZEZm5mUmRESExKUTJHNk1HWUlJbkdobGRqdWRyaXB6QmpuNERwNkxrOWwyU0gyR3V0dk4wU21FcERISnpDZWlPVlZNZzVxcFZuL2VqNjNDeGlNZzhVNXVwTXk4U2FPWEVGOGQ0Ky9kbnJjb090WjF0Yk40eW4vSytWTWJwd25LMHNjRGQyWUsxeEt4Qm1PbDlxeGI1djNKTmRpS3VDMVNQMS9tTm81OUdnelgxeUYxQ2NNeVN4WnRiKzA0SUZBY2QyV0hMS1hFVGllZGFabnpoVklrdVBoenBoV2FRUExHc2JBcmNja1ZJaVljNVpBRGlYdGk2WENmQk1TeEtOdXFpYkZnZmFURTgzOXFsY3NxQm1NYy9ITzMrT1FWSVdBRGR3R2tvQWZ1bk1TNmN1QzMxMW51c2x5MUI4QnQ1c1htNWpUS0dWOHJtZklGa09ybUpUWU1JMDdrUGF2RXo4THpIUFlPSFN1MGFrQkE1bW9weUhHM0pXdGQrR3pnMU53RldEZ0RsamlySmg3UUd3KzJxNmx0ZnZTZmkyVnAvREFXL3JuWTNLOW1RMnJIMkI3Q3doOXpxUDNBR0Y1S3J0V2tTMjg5djArSzh6SXd3SDEzaWw3RGpQVGlpQ3JsbUpGdEtkZ3E2YnpaVEM3WnlSYjgxdDN6QTJsRVB3bW5aRVRwZFpkUXpadDl5a0VOTEE0TjNpbEVJV2l1NHBGZjhZdGtRYkUrN0xyMk1KQktKN2crMmpxR20vcmdFYmtDbnBidy9iUVFsMU02U0hldWd6RVU0VDdYTjViUTVqTFNJamVMWWhuejhPYWNGb0lvYktwdFFONTE5eC9xUjFhOG9LSkQ4bVhKeUVRYzdWdzQrRGhXVUlLT09FdlpMZm1USUgyZmFHYk5rWVgzMGhPLzFkSmg3OVB4cEtucHB1N2RQRjVJbmQ0WEM5WVpudzNPVGtaeGpubjFlUW1zQ3BYSWgza2NjMk41VVQzSWZvT1VXQ0hGZ2dZbTVxeEU5OUpRR2tHVGN1WDcwM05pTGI4ZGxyTGlhcm02bENqTHNyUitLc3lnOVQ2ekY5dGw3eHBQM1hoK05PRkkwL0lWczI5SUo4UXpvcm5SZUwzWFFkYmMvTlJ3MEQzb2VZSm9aNzBDQXZETkFvblBzMTQvVUJqeU52NmlCdG4yM3VjbzlEcmZoQU5MYk1TUEtCa3FHdlhnUlNNY2xoenh3cU01VXpmWTN0VE13MkRKajBTajlyVHh5akI3L3lqYWNmUWRnZkZmRVVuUmkxcURaaEh1akI4cHpPdEwrdExORlJHUlZrL0lWZmFsbktOZnJiMThicnZ5QXh4UFNvbXRxS1lIbTdrQWF0NFJVeitCL3czYVMyVmJ3YVh5c0RDMVl0WGt2M2ZKczlKQ2wyUkp1THBacXVXanhmQ0o4dHV5bkwzYTVFbjNlN1ZDVjJmZjZoNXdySG1JdldYUjdkcUhPY3RDTlkvN1U3emFlRUpoVzI4M1NaZHVWRGsxOVg3NEw0T1A5c0s4allQUGtmSG1sYjh4aWZLNk9yK1dlUEhnS242NDBkby9OZGJ1UHhyZ2JyWXBJdCt1SXU3a3NuYzVESVpZK29PL2QwTmpRbWx2c2R0alhsV2plOTcwZ0tMcURaMTZVVGVKMUdOay9EZ1c4S3F6Q3kydnY4aG8xd3A3dVFNMFIxQXV2UkdmK0w4MUpXajkxOHJzUUhKckc2VkJXUDRWT1pqYkRiOEkzR2VrNkJsbk5VSng4blhGTHRheFBBanN4YjZNeGhZNjQ0d3R3cXFjV3RjTTJuUm1mdis4dEhqN09KZDN5anI2aG10THZSTHd6aFdLcm1FTFRvV2ZvbGVILzdXdDEzd01sblY2akFUM3U1TUVIR3RsNDF1ZSsrZjV0dkJrWmVJbDNJblpDeWZhWUFLOWNBZDlPcy9uQ2FkZ3hhQkMybXpwVjdhVXFlTjRkSGo2Y3ExQUI0VCtRV2VubVhublhZL1Y1N2llamJOZHN2S3lMVisxeEtzS3dCS0NSK3dKellYUmt6Z3h0YnJCSGtXTzV0VENMWDhsS2RwUmhmb3NyZ1ZWNm5EZjVyR1Q3WlZuL09YYW5wenNFZEEyMzNxY2orUkhPakgxM2tReHovekh1eGFKbDI3T1A2TWtvblBpcm9JR0MxSitYcWsxU3FMc2MrMHRhUXkyWUJzSjdERUlmY01ibUpzZm9weW9WVzZWUXBDN0lIL1p6OURjOUNaTG1LV1B0WXhveW52R0RoYmNnRmswdG5xQ2lHT1Q0MHZiZzFRRzVkanJpeUdKanNCTUtlUTkzaVg3MGtDeWNna1RnaXIzaThWTkhBMUpUUW9vL2kxam1IUjVHVjZZY1k5akpsMmVkRGJJWHA3UnVGK0QzOUVpZjhvWXJCaW03d1o3cGVONTBQRFQ4aTRGTHBGQkRyWDRzZlhHSzhWZEhIcDdDSkJUckVTRWVkdUE2MXdhUUM2Tk5LT2psVDRxVkwzYzNlTlVhaTBVWmNBNTBnRlY4U2dmOVB6VUp5Z2hYeWR1VUFRRGpmb2xRUUdSSjZQMFY4QW4weVNQZkR3WWRkNU1uc0g4dTRqK2dyeE56KzRScTFKQ3krUlBkNko3dXROY25jUit4R21iRHpSZ3J5dGxsS1hVSUpsQ1krMHErcnVOcjdiRGhoWmhNWmpWRGR3amQzTzAyekhTWkF0SEppT2NTN1N6L1hNUXZ0cFVqTHcycUI4TFVkVzljZG1JVUxtRm5Pb1lpRlJVRkRLT212b2FOaEhKc01PWUxhWkJEVS9ZNlVxS0tiaFlzelk4dnZTc2t4OFR4RG9mMTlhMm9hQWEybldaRmxMdVRXbDB6NzVPS3J4b2RpSyt2eWxwU25NWmtWc2NvWHdXL0pFLzhwRnduVlBHL043L3IwdmEvVWJlNUNOZnJycHRGRWc2UGVMdnhGUG5CT0Z0aHpGblhRajBSSlRQbjI3T0x4d1pHOEU3eThuaEx4WDdjTVI0bm9TK0o1UE1xbzZvSG1UVi9KbjZSOHBHMkNEd3VKb1V5ZnplbHdnbVBpSDYwVm8rYTJDdENiSFZaQTEwdGgvUVZjd3didmJJY2x0VmNPVVd2ZnF3WmpLVWdBYi9hcHVuTnphMnNPOTNaVGlKWHRzTlVCRkhuWWdvTzRVaFlzWlpTWTRNZE9QVFhHcERNL1RBWEpUQmhibUZ2eW1oeXNPMlQwdG1FTnltZGU1QXpBOHdJaXpPWmJIaEtyQ2txUndZRmJhN241ajkzU3h5QVo1RHhURitIL1BuQ3cvQ1BUbkx0Vkk3NzhpbSsvaCtQbmJiTXdJbGJmOVVVV1lrYnQ2dXptQ0ZFVWs4eWtMOHAyM1hqb2xqS0RoOEp3Zk0wR2pxcnZacU9ZWlZyVHFlUyt1aHJSTEYyMmtXMWp4dmc1cHBqUmtMdmx4WWZoc3ZzSm1LSVpEZmFhU2FuVHZWOVdTSDRPZFg3bGxuWG9qTTV5bVJxRytSZHFWN0t2ZHpacHBUaStoRXlPYVBVRld2VE9FdHhRaDBCMis0RFpoTnhYNEJOMEEzNVpMTld6UTcrbW0vNGlaWGVrc2lTL3UzMEhiTGl6RUNqMFVtbGlUUkkxckloTng5K3lwSWU4SEVRM3owNFR1M3RTSDA3aGRVc1E3SWFLMjB3SStuTDBIdHBUSmNrNVZleDRXVndWZ0NqT0g1bko5a1lkTVgvcGVuVCtNSmZRTzE0QzJOV2RCRkFRcXIyUW14T0F5TjBxa0FId05VZjhNNHcvSTc2Y25WMnhVVHROdERweVEwUDREeVM4SExOYXhYaFR0bFdSdWU5M2dCWTYxZ255SWU5anliN3plTlNZQ1lIdGNyYzIyRk5BaGE0bC9DRlE0Q3k1ekd1V21nV2ZLMmYvdnh5TFJmTmRTaUt1UUVtUmRCcGszU3d1eDR0cTk3encwTno1Qis0SW5WYlAwcldLT3Z6OU9NOGVJMDNtY1NYc0ZHa0JVNHJYU3laczBOaU5LaENTS0E0ZU1GUHlsdFRqbjlGaHJBekhLRnJQd2l5L0xKUTk4Y0pzZC85MXpHeC9PTFhWb0k1NWZpekgvZHIwUEFMZzk0SkQyNnNJQk1Jd2NlZ2I0bmdPZmZ6Q2VXRnV5dnZSbU5ocnhYbG1tTXNxbUlUa1htRExJcTJHdXhKaTdEa2N0UUZaMUU2eGk5eXNoSlQ5dk9aS0V0bEZ4Ym9ncUkyZURTcXRPOWNMdEtrWTJJdHFkTTNWTTdhWVpIbHd3RVlZOVp4TzNpa2tyLzZCQ3Y2YnpQd0pYVm1TRTVkVHMyN1lvdmZ6TWRtQzUwM3VZaVNoQm9YQnpZZ0JTL2ozN0VrZStVVFRlOXdNQUZnMU1WTVUyeVpYZmJzdmF4dm4wWUFPQWxCU1hLL1lqQ1p1MEJHcXIrd2tqeGVlNTF5V1NaYTR2Z1Y4RnpUZFY3VWpFakpQV0ZzTklwMW1aMFFZTUppVnU1RDFXdlJHblY3KzdwNEFCQzd2VG9KNStuNm56clp3aitWVXFvLzM3bHZqQzE4UTIzWGFJbTBpd29SMHBwL1pZWVI1K0Y4Y0JhZDZ2ajlMVzRTanFNQ1hBak16dlZRRmE0T3ljT0g3OXRlRXFHWmt3WCtIbTZkOWVnN0lFeHRoSExhajQ1Z2p0RjV1NE9EVllkZjJLTFpZVnlPREV2dkJUdXQrZTJCd0Z1S3dlakU3d3ozVkhYNFhOeG5lai9aZU1yODV4VXB1OHVENWtIUVVsS0h6MHdhL2R2MlpBdEpkZWVEOE9YWHcxcUp4cW1zWG9zVGI3NmtudlpQQjNNSzZuY3Nac2pGTnMzUFI3MEJJK1BNNW9JUFhpcHltSkEzSGNyYVE3eW9CdmUwTU5BWUkwV0tLQU9kU1hqQXkvOG83RDFyeTlXZHhCTzhVaUEwbm52amZDUlhFTGp1QkhxaE1FRXJpNTVTcHdReEdJNWNuLzJDbTcwdnJ6NHNRWVhMcDUycWZFdWlNd0V0NzF1M2poZVZvZGI3eFArVjR5bDlHYjJERW10QUZpMW1SUFF2c3NQdElrRld5RHFxQm9uTWZrRkxza1hEWEhhNncxeTZ0cVVMZnVKMlBhTnJveUxqbXUyYXhSUUk1MXl4Q2loeWhIRm95Vm9oaG9ka0s1a3JRM3JvaWhic2JsN0RJb1RiWWtTZld2d0RIeHBHQ1JBNDVLUXdNOXoyUmYyemEweVJoS3BldHBzeHUwbTVPSy9oMG5ydjFpRy9pQVh5SVpqVnF0SDNOUXh4cHVuZ3h3ZHpwZGtwOUlkazBpRkpCQnNPbnd2UEFvZXhUT01mbDJnL1ljMkdXRnpzbERFakJYV0tqaGdUL3hXTHhacTBtMW4ydDZRc1hEUUxiVU9CclE2Q0JaTnhlQW9KcDVxREttYUVnNjFHTmF6S2lwNlZMTzNCTnlyZXZLNGx3UnJJT0ZEWHNjRkJPczh4dzUveWM2ZmdZNzBqQi8zRjNhdzR2MmsvRmZJRUlINDdPWWZqQ0ZBS1VPOU50cEdnMUFwZnlickpUUDB3NDJ6RUZiYkRxR1d1MnhQZ21tR0ptMEpJZEZnb2pIRzNzN2Y4bjl6WmxMVDF1MnY5RmhVVmNPb1E3bGtFZGluSDBFY0hmd1c3NXgvZzZYWHlxdW1GVzl3K3RKSVhHczlkcDVzWmkxVS9lUWVGbGVQdFY1Uk10MzJ1Sy8wYkEvL0hGeFBJYjlORmVmaHJQdDF6bjBndWM4TXBLYUJrdEp0QUtPTndwQzhFc3lpUmR5OS81dUZvNVIzNzJ6azBoMXNQcGRXSE9EVE0iLCJzIjoiNWUwOThlMGNiZGJlZGMzMyIsIml2IjoiNmJmOTg1MzAyNTQxYzVjNWFjMGUwZGM5NmI2YjhiNmYifQ=="
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

Cookies = {"RBXEventTrackerV2": ""} # import RBXEventTrackerV2 cookie here
Username = "" # import username here
Password = "" # import password here

def GetCSRF() -> dict:
    Response = Requests.post(url=LOGIN_API)
    return Response.headers["x-csrf-token"]

def DecodeMetadata(MetadataB64: str) -> str:
    return Base64.b64decode(MetadataB64).decode("utf-8")

def FetchToken(DataExchange: str) -> str:
    Data = {
        "bda": ROBLOX_BDA,
        "capi_version": "2.2.2",
        "capi_mode": "inline",
        "data[blob]": DataExchange,
        "public_key": ROBLOX_KEY,
        "rnd": str(Random.random()),
        "site": f"{ROBLOX_URL}/login",
        "style_theme": "default",
        "userbrowser": USER_AGENT
    }
    Headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip/deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": JS_URL,
        "Pragma": "no-cache",
        "Referer": f"{JS_URL}/v2/2.2.2/enforcement.7fe4ebdd37c791e59a12da2c9c38eec6.html",
        "Sec-Fetch-Site": "same-origin",
        "sec-fetch-mode": "cors",
        "User-Agent": USER_AGENT
    }
    Response = Requests.post(url=f"{JS_URL}/fc/gt2/public_key/{ROBLOX_KEY}")
    return Response.text if Response.text != "" else "NO_TOKEN"

def ContinueCaptcha(ChallengeId: str, Metadata: dict, Headers: dict) -> bool:
    Data = {
        "challengeId": ChallengeId,
        "challengeMetadata": JSON.dumps({
            "unifiedCaptchaid": Metadata["unifiedCaptchaId"],
            "captchaToken": Metadata["captchaToken"],
            "actionType": Metadata["actionType"]
        }),
        "challengeType": "captcha"
    }
    Response = Requests.post(url=CONTINUE_API, headers=Headers, cookies=Cookies, json=Data)
    return Response.status_code == 200

def FinishLogin(ChallengeId: str, MetadataB64: str, CSRF: str, Data: str) -> str:
    Headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Rblx-Challenge-Id": ChallengeId,
        "Rblx-Challenge-Metadata": MetadataB64,
        "Rblx-Challenge-Type": "captcha",
        "User-Agent": USER_AGENT,
        "X-Csrf-Token": CSRF
    }
    Response = Requests.post(url=LOGIN_API, headers=Headers, json=Data)
    return Response.cookies.get(".ROBLOSECURITY")

def StartLogin():
    print("[+] Generating CSRF Token")
    CSRF = GetCSRF()
    print(f"[+] Generated CSRF Token: {CSRF}")
    Headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": USER_AGENT,
        "X-Csrf-Token": CSRF
    }
    Data = {
        "ctype": "Username",
        "cvalue": Username,
        "password": Password
    }
    print("[+] Starting login process")
    Response = Requests.post(url=LOGIN_API, headers=Headers, json=Data)
    ResHeaders = Response.headers

    if Response.status_code == 429:
        print("[+] Ratelimited. Waiting a minute to retry.")
        Time.sleep(60)
        return StartLogin()

    ChallengeId = ResHeaders["rblx-challenge-id"]
    MetadataB64 = ResHeaders["rblx-challenge-metadata"]
    print(f"[+] FunCaptcha Challenge ID: {ChallengeId}")
    Metadata = DecodeMetadata(MetadataB64)
    Metadict = JSON.loads(Metadata)

    DataExchange = Metadict["dataExchangeBlob"]
    Blob = {"data[blob]": DataExchange}
    Token = FetchToken(DataExchange)
    Metadict["captchaToken"] = Token
    print(f"[+] FunCaptcha challenge token: {Token}")

    print("[+] Continuing FunCaptcha challenge")
    if ContinueCaptcha(ChallengeId, Metadata=Metadict, Headers=Headers) == True:
        print("[+] FunCaptcha challenge continued successfully")
    else:
        print("[+] FunCaptcha challenge didn't continue")

    TaskId = Funcaptcha.GetTask(Url=ROBLOX_URL, JSUrl=JS_URL, Key=ROBLOX_KEY, Blob=Blob)
    print(f"[+] FunCaptcha TaskId: {TaskId}")
    Result = Funcaptcha.GetResult(TaskId)
    print(f"[+] FunCaptcha Task Result: {str(Result)}")

    SessionCookie = FinishLogin(ChallengeId, MetadataB64=MetadataB64, CSRF=CSRF, Data=Data)
    print(f"[+] Session Cookie: {SessionCookie}")
    
StartLogin()
