Feature: Automatically generate any amount of Tickets and Passes
  @ticket
  Scenario: Buy ticket(s) with/without park admission
    When we buy tickets
    When we buy tickets with park admission

  @pass
  Scenario: Buy pass(es) with/without park admission
    When we buy passes
    When we buy passes with park admission