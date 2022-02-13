from datetime import *
from OS.variables import *


def win10():
    print(f"""\
            
                        {CBlue}....,,:;+ccllll   
          ...,,+:;  cllllllllllllllllll   
    ,cclllllllllll  lllllllllllllllllll   
    llllllllllllll  lllllllllllllllllll   {username}@{hostname}
    llllllllllllll  lllllllllllllllllll   {CEnd}{longueur* "-"}{CBlue}   
    llllllllllllll  lllllllllllllllllll   OS{CEnd} : {systemOS} {system} {uname.machine}{CBlue}
    llllllllllllll  lllllllllllllllllll   UPTIME{CEnd} : {Uptime}{CBlue}
    llllllllllllll  lllllllllllllllllll   Resolution{CEnd} : {screens}{CBlue}
                                          CPU{CEnd} : {cpu}{CBlue} 
    llllllllllllll  lllllllllllllllllll   GPU{CEnd} : {gpu}{CBlue}
    llllllllllllll  lllllllllllllllllll   Memory{CEnd} : {memory}{CBlue}    
    llllllllllllll  lllllllllllllllllll   Disk{CEnd} : {disk}{CBlue}
    llllllllllllll  lllllllllllllllllll   Python{CEnd} : {pythonVersion}{CBlue}
    llllllllllllll  lllllllllllllllllll
    `'ccllllllllll  lllllllllllllllllll
           `' \*::  :ccllllllllllllllll
                           ````''*::cll{CEnd}
    """)
def win11():
    print(f"""\
    {CBeige}################  ################
    ################  ################
    ################  ################   {username}@{hostname}
    ################  ################   {CEnd}{longueur* "-"}{CBeige}
    ################  ################   OS{CEnd} : {systemOS} {system} {uname.machine}{CBeige}
    ################  ################   UPTIME{CEnd} : {Uptime}{CBeige}
    ################  ################   Resolution{CEnd} : {screens}{CBeige} 
                                         CPU{CEnd} : {cpu}{CBeige}
    ################  ################   GPU{CEnd} : {gpu}{CBeige}
    ################  ################   Memory{CEnd} : {memory}{CBeige} 
    ################  ################   Disk{CEnd} : {disk}{CBeige}
    ################  ################   Python{CEnd} : {pythonVersion}{CBeige}
    ################  ################
    ################  ################
    ################  ################{CEnd}
    """)

def win7():
    print(f"""\
{CRed}        ,.=:!!t3Z3z.,
{CRed}       :tt:::tt333EE3
{CRed}       Et:::ztt33EEEL {CGreen}@Ee.,      ..,
{CRed}      ;tt:::tt333EE7 {CGreen};EEEEEEttttt33#   {username}@{hostname}
{CRed}     :Et:::zt333EEQ. {CGreen}$EEEEEttttt33QL   {CEnd}{longueur* "-"}
{CRed}     it::::tt333EEF {CGreen}@EEEEEEttttt33F    {CRed}OS{CEnd} : {systemOS} {system} {uname.machine}
{CRed}    ;3=*^```"*4EEV {CGreen}:EEEEEEttttt33@.    {CGreen}UPTIME{CEnd} : {Uptime}
{CBlue}    ,.=::::!t=., {CRed}` {CGreen}@EEEEEEtttz33QF     {CGreen}Resolution {CEnd} : {screens}
{CBlue}   ;::::::::zt33)   {CGreen}"4EEEtttji3P*      {CBlue}CPU{CEnd} : {cpu}
{CBlue}  :t::::::::tt33.{CYellow}:Z3z..  {CGreen}`` {CYellow},..g.      {CBlue}GPU{CEnd} : {gpu}
{CBlue}  i::::::::zt33F {CYellow}AEEEtttt::::ztF       {CYellow}Memory{CEnd} : {memory}
{CBlue} ;:::::::::t33V {CYellow};EEEttttt::::t3        {CYellow}Disk{CEnd} : {disk}
{CBlue} E::::::::zt33L {CYellow}@EEEtttt::::z3F        {CYellow}Python{CEnd} : {pythonVersion}
{CBlue}(3=*^```"*4E3) {CYellow};EEEtttt:::::tZ`
            {CBlue} ` {CYellow}:EEEEtttt::::z7
                 {CYellow}"VEzjt:;;z>*`{CEnd}
                 """)

def allLinux():
    print(f"""\
           {CBlack}#####
          #######          {CWhite}{username}@{hostname}{CBlack}
          ##{CWhite}O{CBlack}#{CWhite}O{CBlack}##          {CEnd}{longueur* "-"}    
          {CBlack}#{CYellow}#####{CBlack}#          {CWhite}OS{CEnd} : {systemOS} {system} {uname.machine} 
        {CBlack}##{CWhite}##{CYellow}###{CWhite}##{CBlack}##        {CWhite}UPTIME{CEnd} : {Uptime}                   
       {CBlack}#{CWhite}##########{CBlack}##       {CWhite}Resolution{CEnd} : {screens}
      {CBlack}#{CWhite}############{CBlack}##      {CWhite}CPU{CEnd} : {cpu}
      {CBlack}#{CWhite}############{CBlack}###     {CWhite}GPU{CEnd} : {gpu}
    {CYellow}##{CBlack}#{CWhite}###########{CBlack}##{CYellow}#      {CWhite}Memory{CEnd} : {memory}
   {CYellow}######{CBlack}#{CWhite}#######{CBlack}#{CYellow}######   {CWhite}Disk{CEnd} : {disk}
   {CYellow}#######{CBlack}#{CWhite}#####{CBlack}#{CYellow}#######   {CWhite}Python{CEnd} : {pythonVersion}
     {CYellow}#####{CBlack}#######{CYellow}#####{CEnd}
    """)

def apple():
    print(f"""\
                   {CGreen} c.'
                 ,xNMM.
               .OMMMMo
               lMM"
     .;loddo:.  .olloddol;.         {username}@{hostname}
   cKMMMMMMMMMMNWMMMMMMMMMM0:{CYellow}       {CGreen}{longueur* "-"}{CYellow}
 .KMMMMMMMMMMMMMMMMMMMMMMMWd.       {CYellow}OS{CEnd} : {systemOS} {system} {uname.machine}{CYellow}
 XMMMMMMMMMMMMMMMMMMMMMMMX.         {CYellow}UPTIME{CEnd} : {Uptime}{CRed}
;MMMMMMMMMMMMMMMMMMMMMMMM:          {CRed}Resolution{CEnd} : {screens}{CRed} 
:MMMMMMMMMMMMMMMMMMMMMMMM:          {CRed}CPU{CEnd} : {cpu}{CRed}
.MMMMMMMMMMMMMMMMMMMMMMMMX.         {CRed}GPU{CEnd} : {gpu}{CRed}
 kMMMMMMMMMMMMMMMMMMMMMMMMWd.       {CRed}Memory{CEnd} : {memory}{CPurple}
 'XMMMMMMMMMMMMMMMMMMMMMMMMMMk      {CPurple}Disk{CEnd} : {disk}{CPurple}
  'XMMMMMMMMMMMMMMMMMMMMMMMMK.      {CPurple}Python{CEnd} : {pythonVersion}{CBlue}
    kMMMMMMMMMMMMMMMMMMMMMMd
     ;KMMMMMMMWXXWMMMMMMMk.
       "cooc*"    "*coo'"{CEnd}
    """)   
def unknown():
    print(f"""\
           {CGreen} ________
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p                {username}@{hostname}
     "^^"              T####                {CEnd}{longueur* "-"}{CGreen}
                       d###P                {CGreen}OS{CEnd} : {systemOS} {system} {uname.machine}{CGreen}
                    _g###@F                 {CGreen}UPTIME{CEnd} : {Uptime}{CGreen}
                 _gN##@P                    {CGreen}Resolution{CEnd} : {screens}{CGreen} 
               gN###F"                      {CGreen}CPU{CEnd} : {cpu}{CGreen}
              d###F                         {CGreen}GPU{CEnd} : {gpu}{CGreen}
             0###F                          {CGreen}Memory{CEnd} : {memory}{CGreen}
             0###F                          {CGreen}Disk{CEnd} : {disk}{CGreen}
             0###F                          {CGreen}Python{CEnd} : {pythonVersion}{CGreen}
             "NN@'

              ___
             q###r
              ""{CEnd}""")  