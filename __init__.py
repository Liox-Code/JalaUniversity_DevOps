import virtualbox

option = int(input(f"1. Create a VM 2. Delete a VM 3.Stand up a VM"))

machineName = "test"

vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
virtualMachine = vbox.find_machine('vml_default_1668480469401_48295')


if option == 1:
    print("Creating")
    machine = vbox.create_machine(
        "", machineName, ["/test"], "Linux_Ubuntu", "forceOverwrite=1")
    vbox.register_machine(machine)
elif option == 2:
    print("Delete")
    virtualMachine = vbox.find_machine(machineName)
    virtualMachine.remove(delete=True)
elif option == 3:
    print("Stand Up")
    progress = virtualMachine.launch_vm_process(session, 'headless', [])
    progress.wait_for_completion()
    if session.state >= 2:
        session.console.power_down()
        print("Stand Down")
