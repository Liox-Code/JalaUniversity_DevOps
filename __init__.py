import virtualbox

option = int(input(f"1. Create a VM 2. Delete a VM 3.Stand up a VM"))

# vbox = virtualbox.VirtualBox()
# session = virtualbox.Session()
# vmMachine = virtualbox.FindMachine("Windows 8")
# print(vmMachine)
# machine = vbox.find_machine("vml_default_1668480469401_48295")

# if option == 1:
#   print ("Creating")
# elif option == 2:
#   print ("Delete")
#   session.console.power_down()
# elif option == 3:
#   print ("Stand Up")
#   progress = machine.launch_vm_process(session, "headless",[])
#   progress.wait_for_completion()
# elif option == 4:
#   # vmMachine.LockMachine(session, LockType.LockType_Shared);
#   print ("Stand Down")
#   process, unused_variable = session.machine.take_snapshot("snapshot_name", "snapshot_description", False)  
#   process.wait_for_completion(timeout=-1)
#   session.unlock_machine()

# print(session.state)
# # print ([m.name for m in vbox.machines])

vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
vm = vbox.find_machine('vml_default_1668480469401_48295')



if option == 1:
  print ("Creating")
  # machine = VirtualMachine.create("CreateTestVM", "Ubuntu",
forceOverwrite=True)
elif option == 2:
  print ("Delete")
elif option == 3:
  print ("Stand Up")
  progress = vm.launch_vm_process(session, 'headless', [])
  progress.wait_for_completion()
  if session.state >= 2:
    session.console.power_down()

IVirtualBox.create_appliance()